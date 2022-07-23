def fib(num):
    if num == 1 or num == 2:
        return 1
    small_output1 = fib(num-1)
    small_output2 = fib(num-2)
    return small_output1 + small_output2

print(fib(num=5))