'''
# Approch first which time consuming and copied list every time
def isSorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True

    if a[0] > a[1]:
        return False
    smallerList = a[1:]
    smallerListSorted = isSorted(smallerList)
    if smallerListSorted:
        return True
    else:
        return False

a = [1,2,3,7,9,11]
print(isSorted(a))
'''

def is_sorted_better(a,si):
    l = len(a)
    if si == l-1 or si == l:
        return True
    if a[si]>a[si+1]:
        return False
    isSmallerPartSorted = is_sorted_better(a,si+1)
    return isSmallerPartSorted
print(is_sorted_better([1,2,8,4,5,6,8],1))