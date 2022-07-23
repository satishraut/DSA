def Geometric_Sum(n):
    if n == 0:
        return 1
    num = 2 ** n
    return (1 / num) + Geometric_Sum(n - 1)

    pass

print(Geometric_Sum(5))