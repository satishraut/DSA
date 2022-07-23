def fi(arr,k):
    if len(arr)==0:
        return -1
    if arr[0]==k:
        return 0
    so=fi(arr[1:],k)
    if so==-1:
        return -1
    else:
        return 1+so     
n=int(input())
arr=[int(x) for x in input().split()]
k=int(input())
ans=fi(arr,k)
print(ans)