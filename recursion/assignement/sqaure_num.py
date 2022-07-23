def check_power(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return check_power(x,y-1)
a,b = input().split()
a = int(a)
b = int(b)
print(check_power(a,b))