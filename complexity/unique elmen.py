from sys import stdin


def findUnique(arr):
    empt = []
    # Your code goes here

    for i in arr:
        if i in arr:
            continue
        empt.append(i)
        return empt

print(findUnique([10,20,30,10,40]))

