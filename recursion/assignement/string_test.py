import re
def check_string(string):
    return bool(re.fullmatch(r"^a(a|bba)*(bb$)?", string))
input_str = input()
print(check_string(input_str))