def findStep(n):
    if (n < 0):
        return 0
    elif (n == 0):
        return 1
    else:
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)

num = int(input())
print(findStep(num))