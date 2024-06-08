file = open('./enc','r')
flag = file.read()
print(type(flag))
print(flag)
original = flag
flag = 'picoCTF{'
string = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
print(string == original[0:4])
flag = ''.join([chr(ord(original[i]) // 256) + chr(ord(original[i]) % 256) for i in range(len(original))])
print(flag)