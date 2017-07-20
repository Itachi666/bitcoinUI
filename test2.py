""" base58 encoding / decoding functions """
import unittest
import base58
import hashlib
import ecdsa

alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
base_count = len(alphabet)


def encode(num):
    """ Returns num in a base58-encoded string """
    encode = ''

    if (num < 0):
        return ''

    while (num >= base_count):
        mod = num % base_count
        encode = alphabet[mod] + encode
        num = num / base_count

    if (num):
        encode = alphabet[num] + encode

    return encode


def decode(s):
    """ Decodes the base58-encoded string s into an integer """
    decoded = 0
    multi = 1
    s = s[::-1]
    for char in s:
        decoded += multi * alphabet.index(char)
        multi = multi * base_count

    return decoded


class Base58Tests(unittest.TestCase):
    def test_alphabet_length(self):
        self.assertEqual(58, len(alphabet))

    def test_encode_10002343_returns_Tgmc(self):
        result = encode(10002343)
        self.assertEqual('Tgmc', result)

    def test_decode_Tgmc_returns_10002343(self):
        decoded = decode('Tgmc')
        self.assertEqual(10002343, decoded)

    def test_encode_1000_returns_if(self):
        result = encode(1000)
        self.assertEqual('if', result)

    def test_decode_if_returns_1000(self):
        decoded = decode('if')
        self.assertEqual(1000, decoded)

    def test_encode_zero_returns_empty_string(self):
        self.assertEqual('', encode(0))

    def test_encode_negative_number_returns_empty_string(self):
        self.assertEqual('', encode(-100))


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


def extendedGCD1(a, b):
    # a*xi + b*yi = ri
    if b == 0:
        return (1, 0, a)
    (x, y, r) = extendedGCD1(b, a % b)
    tmp = x
    x = y
    y = tmp - (a / b) * y
    return x, y, r


def getadd(x1, y1, x2, y2, q, a=0):
    if x1 == x2 and (y1 + y2) % q == 0:
        return 0, 0
    if x1 == x2 and y1 == y2:
        t, nothing1, nothing2 = extendedGCD1(2 * y1, q)
        lamda = (3 * x1 * x1 + a) * t % q
    else:
        t, nothing1, nothing2 = extendedGCD1(x2 - x1, q)
        lamda = (y2 - y1) * t % q
    print lamda
    x = (lamda ** 2 - x1 - x2) % q
    y = (lamda * (x1 - x) - y1) % q
    return x, y


def getkG(k, x, y, p, a=0):
    s = bin(k)
    m = [[0, 0] for i in range(500)]
    m[0][0] = x
    m[0][1] = y
    for i in range(1, 500):
        m[i][0], m[i][1] = getadd(m[i - 1][0], m[i - 1][1], m[i - 1][0], m[i - 1][1], p, a)
    pkx = 0
    pky = 0
    t = range(2, len(s))
    t.reverse()
    r = 0
    for i in t:
        if s[i] == '1':
            if pkx == 0 and pky == 0:
                pkx = m[r][0]
                pky = m[r][1]
            else:
                pkx, pky = getadd(pkx, pky, m[r][0], m[r][1], p, a)
        r += 1
    return pkx, pky

def privateKeyToPublicKey(s):
    sk = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    return ('\04' + sk.verifying_key.to_string()).encode('hex')

if __name__ == '__main__':
    # unittest.main()
    # print base58.b58encode_int(int('c4461124e648d64fc4f643a6364ab5b11e79fb037e396a5cb5', 16))
    # print encode()
    # print hash160('76a921e44ffe8d0b4a09b12c88a237d6a27992bb6ddd19876377522103b68793892f1dcb7ea2d78f14e993c1f4075b6e483125f691c55fe858fba2e75d2103e87a561b9b18f6003d3da5d42a1d0b09f72cc87b1b84da5438a6507e9c1eba0352ae67772196b2752103501fed2207dfb35ecb665e46ebf32deaddcfe297582d9591db3315dd8aef7ef9ac68')
    # print hex(27386662854462232035617028083013371367167810306938988175)
    x = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
    y = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
    q = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    p = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
    sk = int('18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725', 16)

    #print getkG(sk, x, y, p)
    print getadd(0, 1, x, y, p)
    print x
    print getadd(0, 0, 4, 4, 23)

    print privateKeyToPublicKey('18E14A7B6A307F426A94F8114701E7C8E774E7F9A47E2C2035DB29A206321725')
    '''
    n = 386
    pkx = 0
    pky = 376
    for i in range(1, n):
        pkx, pky = getadd(pkx, pky, 0, 376, 751, -1)
    print pkx, pky
    '''