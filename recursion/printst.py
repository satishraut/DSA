# def print_to_n(num):
#     if num == 0:
#         return
#     print_to_n(num-1)
#     print(num)
#     return
# print(print_to_n(10))

from cgi import print_directory


def print_n_to_1(num):
    if num == 0:
        return
    print(num)
    print_n_to_1(num-1)
print_n_to_1(10)

print("hello how are you?")