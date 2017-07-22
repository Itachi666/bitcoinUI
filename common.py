# !/usr/bin/env python

import re
import sys
import copy
import hashlib
import binascii
import base58
from config import *
from bitcoin import *

def sign_tx(raw_tx, index, privkey, version_byte, hashcode, redem=""):
    if (py_version == 3 and isinstance(re, bytes)) or not re.match('^[0-9a-fA-F]*$', raw_tx):
        raw_tx = safe_hexlify(raw_tx)
        return binascii.unhexlify(sign_tx(raw_tx, index, privkey, hashcode))

    if version_byte in version_dict["pubkeyhash"].values():
        pubkey = privkey_to_pubkey(privkey)
        signing_tx = sign_form(raw_tx, index, mk_pkscript(version_byte, hash160(pubkey)), hashcode)
    elif version_byte in version_dict["scripthash"].values():
        assert redem != "", "Empty string found in parameter redem ."
        signing_tx = sign_form(raw_tx, index, mk_pkscript(version_byte, hash160(redem)), hashcode)
    else:
        raise ValueError("Unknown version_byte: '%s' ." % version_byte)

    rawsig = ecdsa_raw_sign(bytes.fromhex(txhash(signing_tx, hashcode)), privkey)
    sig = der_encode_sig(*rawsig) + dec2byte(hashcode, 1, mode="big-endian")
    json_tx = raw2json(raw_tx)

    if version_byte in version_dict["pubkeyhash"].values():
        json_tx["vin"][index]["scriptSig"]["hex"] = call_len(len(sig)) + sig + call_len(len(pubkey)) + pubkey
    elif version_byte in version_dict["scripthash"].values():
        json_tx["vin"][index]["scriptSig"]["hex"] = deal_sig(json_tx["vin"][index]["scriptSig"]["hex"], sig, redem)
    else:
        raise ValueError("Unknown version_byte: '%s' ." % version_byte)
    return json2raw(json_tx)


def deal_sig(befsig, newsig, redem):
    if not befsig:
        return op_dict["OP_0"][2:] + call_len(len(newsig)) + newsig + call_len(len(redem)) + redem
    else:
        assert befsig[:2] == op_dict["OP_0"][2:]
        part = []
        pos = 2
        lens = len(befsig)
        while pos < lens:
            inlen, inb = read_var_len(befsig[pos:pos + 10])
            pos += inb
            part.append(befsig[pos:pos + inlen])
            pos += inlen
        assert part[-1] == redem
        part.insert(-1, newsig)
        res = op_dict["OP_0"][2:]
        for _, item in enumerate(part):
            res += call_len(len(item)) + item
        return res


def sign_form(raw_tx, index, pkscript, hashcode):
    if isinstance(raw_tx, (str, bytes)):
        return json2raw(sign_form(raw2json(raw_tx), index, pkscript, hashcode))
    nraw_tx = copy.deepcopy(raw_tx)
    for _, perin in enumerate(nraw_tx["vin"]):
        perin["scriptSig"]["hex"] = ""
    nraw_tx["vin"][index]["scriptSig"]["hex"] = pkscript
    if hashcode == SIGHASH_NONE:
        nraw_tx["vout"] = []
    elif hashcode == SIGHASH_SINGLE:
        nraw_tx["vout"] = nraw_tx["vout"][index:index + 1]
    elif hashcode == SIGHASH_ANYONECANPAY:
        nraw_tx["vin"] = nraw_tx["vin"][index:index + 1]
    else:
        pass
    return nraw_tx


def der_encode_sig(v, r, s):
    b1, b2 = safe_hexlify(encode(r, 256)), safe_hexlify(encode(s, 256))
    if len(b1) and b1[0] in '89abcdef':
        b1 = '00' + b1
    if len(b2) and b2[0] in '89abcdef':
        b2 = '00' + b2
    left = '02' + encode(len(b1) // 2, 16, 2) + b1
    right = '02' + encode(len(b2) // 2, 16, 2) + b2
    return '30' + encode(len(left + right) // 2, 16, 2) + left + right


def txhash(raw_tx, hashcode):
    if isinstance(raw_tx, str) and re.match("^[0-9a-fA-F]+$", raw_tx):
        if hashcode:
            return hash256(raw_tx + dec2byte(hashcode, 4))
        else:
            return big2little(hash256(raw_tx))
    else:
        raise TypeError("Invalid raw_tx found. ")


def mk_redem(m, *args):
    n = len(args)
    assert m <= n
    res = op_dict["OP_%s" % m][2:]
    for _, pubkey in enumerate(args):
        res += call_len(len(pubkey)) + pubkey
    res += op_dict["OP_%s" % n][2:] + op_dict["OP_CHECKMULTISIG"][2:]
    return res


def mk_pkscript(version_byte, pk_hash160):
    res = "{0}14{1}".format(op_dict["OP_HASH160"][2:], pk_hash160)
    if version_byte in version_dict["scripthash"].values():
        return "{0}{1}".format(res, op_dict["OP_EQUAL"][2:])
    elif version_byte in version_dict["pubkeyhash"].values():
        return "{0}{1}{2}{3}".format(op_dict["OP_DUP"][2:], res, op_dict["OP_EQUALVERIFY"][2:], op_dict["OP_CHECKSIG"][2:])
    else:
        raise ValueError("Unknown version_byte: '%s' ." % version_byte)


def json2raw(json_tx):
    raw_tx = dec2byte(json_tx["version"], 4)
    raw_tx += dec2var_byte(len(json_tx["vin"]))
    for i, perin in enumerate(json_tx["vin"]):
        raw_tx += big2little(perin["txid"])
        raw_tx += dec2byte(perin["vout"], 4)

        raw_tx += dec2var_byte(len(perin["scriptSig"]["hex"]) // 2)
        raw_tx += perin["scriptSig"]["hex"]
        raw_tx += dec2byte(perin["sequence"], 4)

    raw_tx += dec2var_byte(len(json_tx["vout"]))
    for j, perout in enumerate(json_tx["vout"]):
        value = int(perout["value"] * (10**8)) if isinstance(perout["value"], float) else perout["value"]
        raw_tx += dec2byte(value, 8)
        raw_tx += dec2var_byte(len(perout["scriptPubKey"]["hex"]) // 2)
        raw_tx += perout["scriptPubKey"]["hex"]

    raw_tx += dec2byte(json_tx["locktime"], 4)
    return raw_tx


def raw2json(raw_tx):
    json_tx = {
        "version": byte2dec(raw_tx[:8]),
        "locktime": byte2dec(raw_tx[-8:]),
        "vin": [],
        "vout": []
    }
    ins, inb = read_var_string(raw_tx[8:26])
    nraw_tx = raw_tx[8 + inb:-8]
    for i in range(ins):
        perin = {
            "txid": big2little(nraw_tx[:64]),
            "vout": byte2dec(nraw_tx[64:72])
        }
        siglen, inb = read_var_string(nraw_tx[72:90])
        sigp = 72 + inb + siglen * 2
        perin["scriptSig"] = {"asm": "", "hex": nraw_tx[72 + inb:sigp]}
        perin["sequence"] = byte2dec(nraw_tx[sigp:8 + sigp])
        json_tx["vin"].append(perin)
        nraw_tx = nraw_tx[8 + sigp:]

    outs, inb = read_var_string(nraw_tx[:16])
    nraw_tx = nraw_tx[inb:]
    for j in range(outs):
        perout = {
            "n": j,
            "value": byte2dec(nraw_tx[:16]) / (10**8)
        }
        scrlen, inb = read_var_string(nraw_tx[16:34])
        scrp = 16 + inb + scrlen * 2
        perout["scriptPubKey"] = {"asm": "", "hex": nraw_tx[16 + inb:scrp]}
        perout["type"] = "pubkeyhash" if scrlen == 25 else "scripthash"
        json_tx["vout"].append(perout)
        nraw_tx = nraw_tx[scrp:]
    return json_tx


def get_address(version_byte, instr):
    tmp = version_byte[2:] + instr
    res = tmp + hash256(tmp)[:8]
    if version_byte == version_dict["main"]["pubkeyhash"]:
        return "1" + change_base(res, 256, 58)
    else:
        return change_base(res, 256, 58)


def check_address(address):
    res = safe_hexlify(change_base(address, 58, 256))
    if address.startswith("1"):
        res = "00" + res
    if hash256(res[:-8])[:8] != res[-8:]:
        raise ValueError("Invalid address to parse .")
    return res[2:-8]


def change_base(instr, bef, aft, minlen=0):
    if bef == aft:
        try:
            return code_strings[bef][0] * (minlen - len(instr)) + instr if minlen > len(instr) else instr
        except Exception as e:
            raise e
    else:
        return encode(decode(instr, bef), aft, minlen)





def hash160(instr):
    return bin_ripemd160(bin_sha256(instr))


def hash256(instr):
    return bin_sha256(bin_sha256(instr))


def bin_ripemd160(instr):
    res = hashlib.new("ripemd160")
    res.update(bytearray.fromhex(instr))
    return res.hexdigest()


def bin_sha256(instr):
    return hashlib.sha256(bytearray.fromhex(instr)).hexdigest()


def dec2byte(num, byte=None, mode="little-endian"):
    if byte is None:
        res = "{:x}".format(num)
        res = "0" + res if len(res) % 2 == 1 else res
    else:
        res = ("{:0%sx}" % (2 * byte)).format(num)
    return big2little(res) if mode == "little-endian" else res


def byte2dec(byte, num=None, mode="little-endian"):
    res = big2little(byte) if mode == "little-endian" else byte
    if num is None:
        return int(res, 16)
    else:
        return ("%0" + "%sd" % (2 * num)) % int(res, 16)


def big2little(bigstr):
    return "".join([bigstr[2 * i:2 * i + 2] for i in range(len(bigstr) // 2)][::-1])


def dec2var_byte(num):
    num = int(num)
    if num < 253:
        return dec2byte(num)
    elif num < 65536:
        return dec2byte(253) + dec2byte(num, 2)
    elif num < 4294967296:
        return dec2byte(254) + dec2byte(num, 4)
    else:
        return dec2byte(255) + dec2byte(num, 8)


def read_var_string(instr):
    tmp = int(instr[:2], 16)
    if tmp < 253:
        return tmp, 2
    else:
        inb = pow(2, tmp - 251)
        return byte2dec(instr[2:2 + inb]), inb + 2


def call_len(num):
    num = int(num) // 2
    if num <= 75:
        return dec2byte(num)
    elif num < 256:
        return dec2byte(76) + dec2byte(num)
    elif num < 65536:
        return dec2byte(77) + dec2byte(num, 2)
    else:
        return dec2byte(78) + dec2byte(num, 4)


def read_var_len(instr):
    tmp = int(instr[:2], 16)
    if tmp <= 75:
        return tmp * 2, 2
    else:
        inb = pow(2, tmp - 75)
        return byte2dec(instr[2:2 + inb]) * 2, inb + 2

def pkHash(pk):
    m = bin_sha256(pk)
    m = bin_ripemd160(m)

    k = bin_sha256('6f' + m)
    k = bin_sha256(k)

    m = '6f' + m + k[:8]
    if m[0] == '0' and m[1] == '0':
        m = '1' + base58.b58encode_int(int(m, 16))
    else:
        m = base58.b58encode_int(int(m, 16))
    return m

def sig_transaction(txhex0,priv):
    txhex0_hash = hash256(txhex0)
    v,r,s = ecdsa_raw_sign(txhex0_hash,priv)
    return v,r,s


'''redeem1='20fdc304802828d176db677f47e0471d8bfd48951bd525a76387e83aaff2a8fc4220fdc304802828d176db677f47e0471d8bfd48951bd525a76387e83aaff2a8fc42872103e87a561b9b18f6003d3da5d42a1d0b09f72cc87b1b84da5438a6507e9c1eba03ac'
hash1=hash160(redeem1)
hash1='c4'+hash1
hashre1=hash256(hash1)[:8]
hashr1=hash1+hashre1
print base58.b58encode_int(int(hashr1,16))
testjson={
  "txid": "819bd438381c5b7c6634c4c3b5c35d9684b6e87e37211fe9dab8465e44ddfb8c",
  "hash": "819bd438381c5b7c6634c4c3b5c35d9684b6e87e37211fe9dab8465e44ddfb8c",
  "size": 85,
  "vsize": 85,
  "version": 1,
  "locktime": 0,
  "vin": [
    {
      "txid": "47c323b66dd424ccbaacdfd75568b5321a57745ca41843f5a9110f2e1a533fd0",
      "vout": 0,
      "scriptSig": {
        "asm": "",
        "hex": "20fdc204802828d176db677f47e0471d8bfd48951bd525a76387e83aaff2a8fc42"
      },
      "sequence": 4294967295
    }
  ],
  "vout": [
    {
      "value": 1.76000000,
      "n": 0,
      "scriptPubKey": {
        "asm": "OP_DUP OP_HASH160 196c59fb8687000cc413df55f22cdba221a62eab OP_EQUALVERIFY OP_CHECKSIG",
        "hex": "76a914196c59fb8687000cc413df55f22cdba221a62eab88ac",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": [
          "mhqNzF5fQGpeVHpestNbxz8mPDyjzUcSuJ"
        ]
      }
    }
  ]
}
print json2raw(testjson)'''

txhex0 = '0100000001fba480d0b4ac91899b81a9569384162d4339b9da028594ac058b62aac3636696000000001976a91466c3116af03ae7ebcec0c0c597e9b2272bd755a288acffffffff0140237608000000001976a914a962002b56e5a45f4c66facc9cca98346c813e8088ac0000000001000000'
priv = 'cNGtjNKw9y9oVKQDn6RKMsXLuDiaxN3Z7Fb1JPkrCsdbiDNwn6Wy'
v,r,s = sig_transaction(txhex0,priv)
sig1 = der_encode_sig(v,r,s)
print sig1
