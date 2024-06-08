from Crypto.Util.number import inverse
from binascii import hexlify

e = 65537
p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063
n = p * q
print(n)
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
ct = 964354128913912393938480857590969826308054462950561875638492039363373779803642185

m = pow(ct, d, n)
hexBlock = hex(m)[2::]
flag = bytes.fromhex(hexBlock).decode()

print(flag)
