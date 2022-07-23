# in string character other than a keep as it is else replace with b


def replace_string(string,a,b):
    if len(string) == 0:
        return string
    smallerOutput=replace_string(string[1:],a,b)
    if string[0] == a:
        return b + smallerOutput
    return string[0]+smallerOutput

print(replace_string('aa','a','s'))