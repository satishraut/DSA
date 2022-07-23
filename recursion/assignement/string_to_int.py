def stringToInt(str):
    for i in str:
        if type(i)==str:
            str=str.replace("")
    if (len(str) == 1):
        return ord(str[0]) - ord('0')

    y = stringToInt(str[1:])

    # First digit of the number
    x = ord(str[0]) - ord('0')

    x = x * (10 ** (len(str) - 1)) + y
    return int(x)
string = input()
print(stringToInt(string))
