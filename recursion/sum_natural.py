def sum_n(num):
    if num == 0:
        return 0
    return num + sum_n(num-1)

print(sum_n(5))