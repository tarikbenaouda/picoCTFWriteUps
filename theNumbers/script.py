numbers = [
    16,
    9,
    3,
    15,
    3,
    20,
    6,
    "{",
    20,
    8,
    5,
    14,
    21,
    13,
    2,
    5,
    18,
    19,
    13,
    1,
    19,
    15,
    14,
    "}",
]
for index, number in enumerate(numbers):
    if isinstance(number, int):
        numbers[index] = chr(number + 64)
flag = "".join(numbers)
print(flag)
