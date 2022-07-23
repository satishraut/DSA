from sys import setrecursionlimit
setrecursionlimit(10**6) 
def mul(m, n):
    if n==0:
        return 0
    smalloutput=mul(m,n-1)
    return m+smalloutput
    # if (n > 0):
    #     return m + mul(m, n - 1)
    # elif (n < 0):
    #     return -m + mul(m, n + 1)
    # else:
    #     return 0


m = int(input())
n = int(input())
print(mul(m, n))