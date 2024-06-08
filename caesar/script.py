enc_flag = "picoCTF{ynkooejcpdanqxeykjrbdofgkq}"
enc_flag_trim = "ynkooejcpdanqxeykjrbdofgkq"


def charToNum(st):
    result = []
    for c in st:
        result += [ord(c) - 96]
    return result


def numToChar(arr):
    result = ""
    for el in arr:
        result += chr(el + 96)
    return result


def shift(arr, num):
    for i, el in enumerate(arr):
        x = (el + num) % 26
        if x == 0:
            x = 26
        arr[i] = x
    return arr


for _ in range(1, 26):
    print("flag", _, ":", numToChar(shift(charToNum(enc_flag_trim), _)))
