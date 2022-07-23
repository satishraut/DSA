# Add * if identical charter is found
def a(string):
    if len(string) <= 1:
        return string
    temp = a(string[1:])
    if string[0] == string[1]:
        return string[0] + "*" + temp
    else:
        return string[0] + temp

string = input()
print(a(string))