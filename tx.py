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
    return base58.b58encode_int(int(address_16, 16))


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
        k = s[0:2] + k
        s = s[2:]
    return k


def getaddress(redeem):
    m = bin_sha256(redeem)
    m = bin_ripemd160(m)

    k = bin_sha256('6f' + m)
    k = bin_sha256(k)

    m = 'c4' + m + k[:8]
    m = base58.b58encode_int(int(m, 16))
    return m


def createscriptpubkey(output_type, pubkey_or_redeemscript):
    if output_type == 0:  # p2pkh
        pubkey = pubkey_or_redeemscript
        scriptpubkey = '76a914' + hash160(pubkey) + '88ac'
    if output_type == 1:  # p2sh
        redeemscript = pubkey_or_redeemscript
        scriptpubkey = 'a914' + hash160(redeemscript) + '87'
    return scriptpubkey


def createfundingtx_redeemscript(h, pkb, pkam, nsequence):
    redeemscript = 'a914' + hash160(
        h) + '87635221' + pkb + '21' + pkam + '52ae6708' + nsequence + 'b27521' + pkb + 'ac68'
    # OP_HASH160 Hash160(h) OP_EQUAL OP_IF OP_2 < pkb > < pkam > OP_2 OP_CHECKMULTISIG OP_ELSE < nsequence > OP_CHECKSEQUENCEVERIFY OP_DROP < pkb > OP_CHECKSIG OP_ENDIF
    return redeemscript


def createcommitmenttx_redeemscript(h, pka, pkbm, nsequence):
    redeemscript = 'a914' + hash160(
        h) + '87635221' + pka + '21' + pkbm + '52ae6708' + nsequence + 'b27521' + pka + 'ac68'
    # OP_HASH160 Hash160(h) OP_EQUAL OP_IF OP_2 < pka > < pkbm > OP_2 OP_CHECKMULTISIG OP_ELSE < nsequence > OP_CHECKSEQUENCEVERIFY OP_DROP < pka > OP_CHECKSIG OP_ENDIF
    return redeemscript


def createfundingtx_hex0(vin, fundingtx_1, fundingtx_2, fundingtx_3, pk):
    scriptpubkey = createscriptpubkey(0, pk)
    if vin == 0:
        fundingtx_hex0 = fundingtx_1 + dec2var_byte(
            len(scriptpubkey) // 2) + scriptpubkey + fundingtx_2 + '00' + fundingtx_3 + '01000000'
    else:
        fundingtx_hex0 = fundingtx_1 + '00' + fundingtx_2 + dec2var_byte(
            len(scriptpubkey) // 2) + scriptpubkey + fundingtx_3 + '01000000'
    return fundingtx_hex0


def createp2shinputtx_hex0(p2shinputtx_1, p2shinputtx_2, redeemscript):
    p2shinputtx_hex0 = p2shinputtx_1 + dec2var_byte(len(redeemscript) // 2) + redeemscript + p2shinputtx_2 + '01000000'
    return p2shinputtx_hex0


def sign_transaction(txhex0, sk):
    txhex0_hash = hash256(txhex0)
    v, r, s = ecdsa_raw_sign(txhex0_hash, sk)
    return der_encode_sig(v, r, s) + dec2byte(0x01, 1, mode="big-endian")


def createfundingtx(pre_txid1, voutx1, pre_txid2, voutx2, z, ha, pkb, pkam, nsequence):
    n_version = '01000000'
    vin = '02'
    vin_hash1 = backstr(pre_txid1)
    if voutx1 == 0:
        vin_n1 = '00000000'
    else:
        vin_n1 = '01000000'
    vin_nsequence1 = 'ffffffff'
    vin_hash2 = backstr(pre_txid2)
    if voutx2 == 0:
        vin_n2 = '00000000'
    else:
        vin_n2 = '01000000'
    vin_nsequence2 = 'ffffffff'
    vout = '01'
    vout_value = hex(int(z * 200000000))
    vout_value = vout_value[2:]
    while len(vout_value) < 16:
        vout_value = '0' + vout_value
    vout_value = backstr(vout_value)
    redeemscripta = createfundingtx_redeemscript(ha, pkb, pkam, nsequence)
    vout_scriptpubkey = createscriptpubkey(1, redeemscripta)
    vout_scriptpubkeylen = dec2var_byte(len(vout_scriptpubkey) // 2)
    nlocktime = '00000000'
    fundingtx_1 = n_version + vin + vin_hash1 + vin_n1
    fundingtx_2 = vin_nsequence1 + vin_hash2 + vin_n2
    fundingtx_3 = vin_nsequence2 + vout + vout_value + vout_scriptpubkeylen + vout_scriptpubkey + nlocktime
    fundingtx = fundingtx_1 + '00' + fundingtx_2 + '00' + fundingtx_3
    txidfundingtx = hash256(fundingtx)
    return fundingtx, txidfundingtx, redeemscripta, fundingtx_1, fundingtx_2, fundingtx_3


def createcommitmenttx(txidfundingtx, voutx, z, pkam, h, pka, pkbm, nsequence):
    n_version = '01000000'
    vin = '01'
    vin_hash = backstr(txidfundingtx)
    if voutx == 0:
        vin_n = '00000000'
    else:
        vin_n = '01000000'
    vin_nsequence = 'ffffffff'
    vout = '02'
    vout_value1 = hex(int(z * 100000000))
    vout_value1 = vout_value1[2:]
    while len(vout_value1) < 16:
        vout_value1 = '0' + vout_value1
    vout_value1 = backstr(vout_value1)
    vout_scriptpubkey1 = createscriptpubkey(0, pkam)
    vout_scriptpubkeylen1 = dec2var_byte(len(vout_scriptpubkey1) // 2)
    vout_value2 = hex(int(z * 100000000))
    vout_value2 = vout_value2[2:]
    while len(vout_value2) < 16:
        vout_value2 = '0' + vout_value2
    vout_value2 = backstr(vout_value2)
    redeemscriptb = createcommitmenttx_redeemscript(h, pka, pkbm, nsequence)
    vout_scriptpubkey2 = createscriptpubkey(1, redeemscriptb)
    vout_scriptpubkeylen2 = dec2var_byte(len(vout_scriptpubkey2) // 2)
    nlocktime = '00000000'
    commitmenttx_1 = n_version + vin + vin_hash + vin_n
    commitmenttx_2 = vin_nsequence + vout + vout_value1 + vout_scriptpubkeylen1 + vout_scriptpubkey1 + vout_value2 + vout_scriptpubkeylen2 + vout_scriptpubkey2 + nlocktime
    commitmenttx = commitmenttx_1 + '00' + commitmenttx_2
    txidcommitmenttx = hash256(commitmenttx)
    return commitmenttx, txidcommitmenttx, redeemscriptb, commitmenttx_1, commitmenttx_2


def createone2onetx(pre_txid, voutx, value, pk):
    n_version = '01000000'
    vin = '01'
    vin_hash = backstr(pre_txid)
    if voutx == 0:
        vin_n = '00000000'
    else:
        vin_n = '01000000'
    vin_nsequence = 'ffffffff'
    vout = '01'
    vout_value = hex(int(value * 100000000))
    vout_value = vout_value[2:]
    while len(vout_value) < 16:
        vout_value = '0' + vout_value
    vout_value = backstr(vout_value)
    vout_scriptpubkey = createscriptpubkey(0, pk)
    vout_scriptpubkeylen = dec2var_byte(len(vout_scriptpubkey) // 2)
    nlocktime = '00000000'
    one2onetx_1 = n_version + vin + vin_hash + vin_n
    one2onetx_2 = vin_nsequence + vout + vout_value + vout_scriptpubkeylen + vout_scriptpubkey + nlocktime
    one2onetx = one2onetx_1 + '00' + one2onetx_2
    txidone2onetx = hash256(one2onetx)
    return one2onetx, txidone2onetx, one2onetx_1, one2onetx_2


def sign_fundingtransaction(fundingtx_1, fundingtx_2, fundingtx_3, pka, ska, pkb, skb):
    siga = sign_transaction(createfundingtx_hex0(0, fundingtx_1, fundingtx_2, fundingtx_3, pka), ska)
    sigb = sign_transaction(createfundingtx_hex0(1, fundingtx_1, fundingtx_2, fundingtx_3, pkb), skb)
    scriptsig1 = call_len(len(siga)) + siga + call_len(len(pka)) + pka
    scriptsig2 = call_len(len(sigb)) + sigb + call_len(len(pkb)) + pkb
    sign_fundingtransaction = fundingtx_1 + dec2var_byte(
        len(scriptsig1) // 2) + scriptsig1 + fundingtx_2 + dec2var_byte(len(scriptsig2) // 2) + scriptsig2 + fundingtx_3
    txid1 = backstr(hash256(sign_fundingtransaction))
    return sign_fundingtransaction, siga, sigb, txid1


def sign_commitmenttransaction(commitmenttx_1, commitmenttx_2, ska, skb, redeemscripta, ha):
    sigam = sign_transaction(createp2shinputtx_hex0(commitmenttx_1, commitmenttx_2, redeemscripta), ska)
    sigb1 = sign_transaction(createp2shinputtx_hex0(commitmenttx_1, commitmenttx_2, redeemscripta), skb)
    scriptsig = '00' + call_len(len(sigb1)) + sigb1 + call_len(len(sigam)) + sigam + call_len(len(ha)) + ha + call_len(
        len(redeemscripta)) + redeemscripta
    sign_commitmenttransaction = commitmenttx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig + commitmenttx_2
    txid2 = backstr(hash256(sign_commitmenttransaction))
    return sign_commitmenttransaction, sigam, sigb1, txid2


def sign_timeoutcommitmenttransaction(one2onetx_1, one2onetx_2, skb, redeemscripta, ha1):
    sigb2 = sign_transaction(createp2shinputtx_hex0(one2onetx_1, one2onetx_2, redeemscripta), skb)
    scriptsig = call_len(len(sigb2)) + sigb2 + call_len(len(ha1)) + ha1 + call_len(len(redeemscripta)) + redeemscripta
    sign_timeoutcommitmenttransaction = one2onetx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig + one2onetx_2
    txid3 = backstr(hash256(sign_timeoutcommitmenttransaction))
    return sign_timeoutcommitmenttransaction, sigb2, txid3


def sign_deliverytransaction(one2onetx_1, one2onetx_2, ska, skb, redeemscriptb, hb):
    siga1 = sign_transaction(createp2shinputtx_hex0(one2onetx_1, one2onetx_2, redeemscriptb), ska)
    sigbm = sign_transaction(createp2shinputtx_hex0(one2onetx_1, one2onetx_2, redeemscriptb), skb)
    scriptsig = '00' + call_len(len(siga1)) + siga1 + call_len(len(sigbm)) + sigbm + call_len(len(hb)) + hb + call_len(
        len(redeemscriptb)) + redeemscriptb
    sign_deliverytransaction = one2onetx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig + one2onetx_2
    txid4 = backstr(hash256(sign_deliverytransaction))
    return sign_deliverytransaction, siga1, sigbm, txid4


def sign_timeoutdeliverytransaction(one2onetx_1, one2onetx_2, ska, redeemscriptb, hb1):
    siga2 = sign_transaction(createp2shinputtx_hex0(one2onetx_1, one2onetx_2, redeemscriptb), ska)
    scriptsig = call_len(len(siga2)) + siga2 + call_len(len(hb1)) + hb1 + call_len(len(redeemscriptb)) + redeemscriptb
    sign_timeoutdeliverytransaction = one2onetx_1 + dec2var_byte(len(scriptsig) // 2) + scriptsig + one2onetx_2
    txid5 = backstr(hash256(sign_timeoutdeliverytransaction))
    return sign_timeoutdeliverytransaction, siga2, txid5
