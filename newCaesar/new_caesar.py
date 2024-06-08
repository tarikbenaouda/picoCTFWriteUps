import string
from ptrlib import chunks

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


# reverse of b16_encode()
def b16_decode(cipher):
    cipher = chunks(cipher, 2)
    plain = ""
    for twoC in cipher:
        binary = bin(ALPHABET.index(twoC[0]))[2:].zfill(4) + bin(
            ALPHABET.index(twoC[1])
        )[2:].zfill(4)
        plain += chr(int(binary, 2))
    return plain


##########################################################################################
##########################################################################################
def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET  # 0<= t1 <= 15
    t2 = ord(k) - LOWERCASE_OFFSET  # 0 <= t2 <= 15
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


# reverse of shift()
def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET  # 0<= t1 <= 15
    t2 = 16 - (ord(k) - LOWERCASE_OFFSET)  # 0 <= t2 <= 15
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


flag = "picoCTF{tarikbenaouda}"  # Modified from "redacted"
key = "e"  # Modified from "redacted"
# assert all([k in ALPHABET for k in key]) # I don't need it anymore
# assert len(key) == 1 # I don't need it anymore

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
    # enc += shift(c, key[i % len(key)]) 'cause len(key==1)
    enc += shift(c, key)

print(enc)


# start decrypting

enc = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"
b16 = ""
for k in ALPHABET:
    b16 = ""
    for c in enc:
        b16 += unshift(c, k)

    flag = "picoCTF{" + b16_decode(b16) + "}"
    print(flag)
