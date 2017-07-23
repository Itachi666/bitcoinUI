import re
import sys
import copy
import hashlib
import binascii
import base58
from config import *
from bitcoin import *

def hash160(instr):
    return bin_ripemd160(bin_sha256(instr))

def big2little(bigstr):
    return "".join([bigstr[2 * i:2 * i + 2] for i in range(len(bigstr) // 2)][::-1])

def hash256(instr):
    return bin_sha256(bin_sha256(instr))


def bin_ripemd160(instr):
    res = hashlib.new("ripemd160")
    res.update(bytearray.fromhex(instr))
    return res.hexdigest()


def bin_sha256(instr):
    return hashlib.sha256(bytearray.fromhex(instr)).hexdigest()

def base68to10(str):
    return base58.b58decode_int(str)

def dec2byte(num, byte=None, mode="little-endian"):
    if byte is None:
        res = "{:x}".format(num)
        res = "0" + res if len(res) % 2 == 1 else res
    else:
        res = ("{:0%sx}" % (2 * byte)).format(num)
    return big2little(res) if mode == "little-endian" else res

def get_address(redeem):
    hash_redeem = hash160(redeem)
    hash_redeem_plus = 'c4' + hash_redeem
    check_sum = hash256(hash_redeem_plus)[:8]
    address_16 = hash_redeem_plus + check_sum
    return base58.b58encode_int(int(address_16,16))

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

def backstr(s):
    k = ''
    while s != '':
        k = s[0:2]+k
        s=s[2:]
    return k

def getaddress(redeem):
    m = bin_sha256(redeem)
    m = bin_ripemd160(m)

    k = bin_sha256('6f' + m)
    k = bin_sha256(k)

    m = 'c4' + m + k[:8]
    m = base58.b58encode_int(int(m, 16))
    return m

def createfundingtx(pre_txid1,voutx1,pre_txid2,voutx2,value,redeemscript):
    n_version = '01000000'
    vin = '02'
    vin_hash1 = backstr(pre_txid1)
    vin_n1 = voutx1
    vin_nsequence1 = 'ffffffff'
    vin_hash2 = backstr(pre_txid2)
    vin_n2 = voutx2
    vin_nsequence2 = 'ffffffff'
    vout = '01'
    vout_value = hex(int(value * 100000000))
    vout_value = vout_value[2:]
    while len(vout_value) < 16:
        vout_value = '0' + vout_value
    vout_value = backstr(vout_value)
    vout_scriptpubkey = createscriptpubkey(1,redeemscript)
    vout_scriptpubkeylen = dec2var_byte(len(vout_scriptpubkey)//2)
    nlocktime = '00000000'
    fundingtx_1 = n_version + vin + vin_hash1 + vin_n1
    fundingtx_2 = vin_nsequence1 + vin_hash2 + vin_n2
    fundingtx_3 = vin_nsequence2 + vout + vout_value + vout_scriptpubkeylen + vout_scriptpubkey + nlocktime
    fundingtx = fundingtx_1 + '00' + fundingtx_2 + '00' + fundingtx_3
    return fundingtx,fundingtx_1,fundingtx_2,fundingtx_3

def createcommitmenttx(pre_txid,voutx,value1,pk,value2,redeemscript):
    n_version = '01000000'
    vin = '01'
    vin_hash = backstr(pre_txid)
    vin_n = voutx
    vin_nsequence = 'ffffffff'
    vout = '02'
    vout_value1 = hex(int(value1 * 100000000))
    vout_value1 = vout_value1[2:]
    while len(vout_value1) < 16:
        vout_value1 = '0' + vout_value1
    vout_value1 = backstr(vout_value1)
    vout_scriptpubkey1 = createscriptpubkey(0,pk)
    vout_scriptpubkeylen1 = dec2var_byte(len(vout_scriptpubkey1) // 2)
    vout_value2 = hex(int(value2 * 100000000))
    vout_value2 = vout_value2[2:]
    while len(vout_value2) < 16:
        vout_value2 = '0' + vout_value2
    vout_value2 = backstr(vout_value2)
    vout_scriptpubkey2 = createscriptpubkey(1,redeemscript)
    vout_scriptpubkeylen2 = dec2var_byte(len(scriptpubkey2) // 2)
    nlocktime = 00000000
    commitmenttx_1 = n_version + vin + vin_hash + vin_n
    commitmenttx_2 = vin_nsequence + vout + vout_value1 + vout_scriptpubkeylen1 + vout_scriptpubkey1 + vout_value2 + vout_scriptpubkeylen2 + vout_scriptpubkey2 + nlocktime
    commitmenttx = commitmenttx_1 + '00' + commitmenttx_2
    return commitmenttx,commitmenttx_1,commitmenttx_2

def createone2onetx(pre_txid,voutx,value,pk):
    n_version = '01000000'
    vin = '01'
    vin_hash = backstr(pre_txid)
    vin_n = voutx
    vin_nsequence = 'ffffffff'
    vout = '01'
    vout_value = hex(int(value * 100000000))
    vout_value = vout_value[2:]
    while len(vout_value) < 16:
        vout_value = '0' + vout_value
    vout_value = backstr(vout_value)
    vout_scriptpubkey = createscriptpubkey(0,pk)
    vout_scriptpubkeylen = dec2var_byte(len(vout_scriptpubkey) // 2)
    nlocktime = '00000000'
    one2onetx_1 = n_version + vin + vin_hash + vin_n
    one2onetx_2 = vin_nsequence + vout + vout_value + vout_scriptpubkeylen + vout_scriptpubkey + nlocktime
    one2onetx = one2onetx_1 + '00' + one2onetx_2
    return one2onetx,one2onetx_1,one2onetx_2

def createscriptpubkey(output_type,pubkey_or_redeemscript):
    if output_type == 0: #p2pkh
        pubkey = pubkey_or_redeemscript
        scriptpubkey = '76a914' + hash160(pubkey) + '88ac'
    if output_type == 1: #p2sh
        redeemscript = pubkey_or_redeemscript
        scriptpubkey = 'a914' + hash160(redeemscript) + '87'
    return scriptpubkey

def createfundingtx_redeemscript(h,pkb,pkam,nsequence):
    redeemscript = 'a914' + hash160(h) + '87635221' + pkb + '21' + pkam +'52ae6708' + nsequence + 'b27521' + pkb + 'ac68'
    #OP_HASH160 Hash160(h) OP_EQUAL OP_IF OP_2 < pkb > < pkam > OP_2 OP_CHECKMULTISIG OP_ELSE < nsequence > OP_CHECKSEQUENCEVERIFY OP_DROP < pkb > OP_CHECKSIG OP_ENDIF
    return redeemscript

def createcommitmenttx_redeemscript(h,pka,pkbm,nsequence):
    redeemscript = 'a914' + hash160(h) + '87635221' + pka + '21' + pkbm + '52ae6708' + nsequence + 'b27521' + pka + 'ac68'
    # OP_HASH160 Hash160(h) OP_EQUAL OP_IF OP_2 < pka > < pkbm > OP_2 OP_CHECKMULTISIG OP_ELSE < nsequence > OP_CHECKSEQUENCEVERIFY OP_DROP < pka > OP_CHECKSIG OP_ENDIF
    return redeemscript

def createfundingtx_hex0(vin,fundingtx_1,fundingtx_2,fundingtx_3,pk):
    scriptpubkey = createscriptpubkey(0,pk)
    if vin == 0:
        fundingtx_hex0 = fundingtx_1 + dec2var_byte(len(scriptpubkey) // 2) + scriptpubkey + fundingtx_2 + '00' + fundingtx_3 + '01000000'
    else:
        fundingtx_hex0 = fundingtx_1 + '00' + fundingtx_2 + dec2var_byte(len(scriptpubkey) // 2) + scriptpubkey + fundingtx_3 + '01000000'
    return fundingtx_hex0

def createp2shinputtx_hex0(p2shinputtx_1,p2shinputtx_2,redeemscript):
    p2shinputtx_hex0 = p2shinputtx_1 + dec2var_byte(len(redeemscript) // 2) + redeemscript + p2shinputtx_2 + '01000000'
    return p2shinputtx_hex0

def sign_transaction(txhex0,sk):
    txhex0_hash = hash256(txhex0)
    v,r,s = ecdsa_raw_sign(txhex0_hash,sk)
    return der_encode_sig(v,r,s) + dec2byte(0x01, 1, mode="big-endian")

def sign_fundingtransaction(fundingtx_1,fundingtx_2,fundingtx_3,pk1,sk1,pk2,sk2):
    sig1 = sign_transaction (createfundingtx_hex0(0,fundingtx_1,fundingtx_2,fundingtx_3),sk1)
    sig2 = sign_transaction (createfundingtx_hex0(1,fundingtx_1,fundingtx_2,fundingtx_3),sk2)
    scriptsig1 = call_len(len(sig1)) + sig1 + callen(len(pk1)) + pk1
    scriptsig2 = call_len(len(sig2)) + sig2 + callen(len(pk2)) + pk2
    sign_fundingtransaction = fundingtx_1 + dec2var_byte(len(scriptsig1) // 2) + scriptsig1 + fundingtx_2 + dec2var_byte(len(scriptsig2) // 2) + scriptsig2 +fundingtx_3
    return sign_fundingtransaction

def sign_commitmenttransaction(commitmenttx_1,commitmenttx_2,sk1,sk2,redeemscript,h):
    sig1 = sign_transaction (createp2shinputtx_hex0(commitmenttx_1,commitmenttx_2,redeemscript),sk1)
    sig2 = sign_transaction (createp2shinputtx_hex0(commitmenttx_1,commitmenttx_2,redeemscript),sk2)
    scriptsig = '00' + call_len(len(sig2)) + sig2 + call_len(len(sig1)) + sig1 +call_len(len(h)) + h + call_len(len(redeemscript)) + redeemscript
    sign_commitmenttransaction = commitmenttx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig + commitmenttx_2
    return sign_commitmenttransaction

def sign_timeoutcommitmenttransaction(one2onetx_1,one2onetx_2,sk,redeemscript,h1):
    sig = sign_transaction(createp2shinputtx_hex0(one2onetx_1,one2onetx_2,redeemscript),sk)
    scriptsig = call_len(len(sig)) + sig + call_len(len(h1)) + h1 + call_len(redeemscript) + redeemscript
    sign_timeoutcommitmenttransaction = one2onetx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig +  one2onetx_2
    return sign_timeoutcommitmenttransaction

def sign_deliverytransaction(one2onetx_1,one2onetx_2,sk1,sk2,redeemscript,h):
    sig1 = sign_transaction(createp2shinputtx_hex0(one2onetx_1,one2onetx_2,redeemscript),sk1)
    sig2 = sign_transaction(createp2shinputtx_hex0(one2onetx_1,one2onetx_2,redeemscript),sk2)
    scriptsig = '00' + call_len(len(sig2)) + sig2 + call_len(len(sig1)) + sig1 +call_len(len(h)) + h + call_len(len(redeemscript)) + redeemscript
    sign_deliverytransaction = one2onetx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig + one2onetx_2
    return sign_deliverytransaction

def sign_timeoutdeliverytransaction(one2onetx_1,one2onetx_2,sk,redeemscript,h1):
    sig = sign_transaction(createp2shinputtx_hex0(one2onetx_1, one2onetx_2, redeemscript), sk)
    scriptsig = call_len(len(sig)) + sig + call_len(len(h1)) + h1 + call_len(redeemscript) + redeemscript
    sign_timeoutdeliverytransaction = one2onetx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig + one2onetx_2
    return sign_timeoutdeliverytransaction

def createtesttx(pre_txid,voutx,pk,value):
    n_version = '01000000'
    vin = '01'
    vin_hash = backstr(pre_txid)
    vin_n = voutx
    vin_nsequence = 'ffffffff'
    vout = '01'
    vout_value = hex(int(value * 100000000))
    vout_value = vout_value[2:]
    while len(vout_value) < 16:
        vout_value = '0' + vout_value
    vout_value = backstr(vout_value)
    vout_scriptpubkey = createscriptpubkey(0,pk)
    vout_scriptpubkeylen = dec2var_byte(len(vout_scriptpubkey) // 2)
    nlocktime = '00000000'
    testtx_1 = n_version + vin + vin_hash + vin_n
    testtx_2 = vin_nsequence + vout + vout_value + vout_scriptpubkeylen + vout_scriptpubkey + nlocktime
    testtx = testtx_1 + '00' + testtx_2
    return testtx,testtx_1,testtx_2

def createtesttx_redeemscript(h,pk1,pk2,pk3):
    redeemscript = 'a914' + hash160(h) + '87635221' + pk1 + '21' + pk2 +'52ae6721' + pk3 + 'ac68'
    return redeemscript

def createtesttx_hex0(testtx_1,testtx_2,redeemscript):
    testtx_hex0 = testtx_1 + dec2var_byte(len(redeemscript) // 2) + redeemscript + testtx_2 + '01000000'
    return testtx_hex0

def sign_testtransaction(testtx_1,testtx_2,sk1,sk2,redeemscript,h):
    sig1 = sign_transaction (createp2shinputtx_hex0(testtx_1,testtx_2,redeemscript),sk1)
    sig2 = sign_transaction (createp2shinputtx_hex0(testtx_1,testtx_2,redeemscript),sk2)
    scriptsig = '00' + call_len(len(sig2)) + sig2 + call_len(len(sig1)) + sig1 + call_len(len(h)) + h + call_len(len(redeemscript)) + redeemscript
    sign_testtransaction = testtx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig + testtx_2
    return sign_testtransaction

pk1 = '02a9c4cdda23a02c4fa6791545321c60fc5c8ee46e9fd5a63491bf0d11d3d17322'
pk2 = '02a74e5bb3fbf55193d49ea643f9a368a164e1cb2001373c614eea3ad274d2879f'
pk3 = '03e87a561b9b18f6003d3da5d42a1d0b09f72cc87b1b84da5438a6507e9c1eba03'
h = 'fdc304802828d176db677f47e0471d8bfd48951bd525a76387e83aaff2a8fc42'
pre_txid = '6d79d1559a198bcc395e1bf4c80c96bab83a235e7fddd54f2950ac4d9b371cd6'
voutx = '00000000'
value = 0.49
pk = '02a9c4cdda23a02c4fa6791545321c60fc5c8ee46e9fd5a63491bf0d11d3d17322'
sk1 = 'cSaxnL9ZswHtH9a43XVVpDUuZsuGAJExXMMtk7ryky3vgt1hBE5d'
sk2 = 'cNzAs6k7yDqKZdwmWP3a7T23BHTkKbcKZiWvZ1nrmwsd9tuFJhD5'
testtx,testtx_1,testtx_2 = createtesttx(pre_txid,voutx,pk,value)
redeemscript = createtesttx_redeemscript(h,pk1,pk2,pk3)
sign_testtransaction = sign_testtransaction(testtx_1,testtx_2,sk1,sk2,redeemscript,h)
print redeemscript
print sign_testtransaction


























