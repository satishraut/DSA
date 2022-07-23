'''def lastindex(arr,x):
    l = len(arr)
    if l == 0:
        return -1
    sl = arr[1:]
    output = lastindex(sl,x)
    if output != -1:
        return output + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1
n= int(input())
arr = list(int(i) for i in input().split())
x = int(input())
print(lastindex(arr,x))'''

