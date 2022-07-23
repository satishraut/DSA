from sys import stdin


def arrayEquilibriumIndex(arr, n):
    left = [0] * len(arr)
    for i in range(1, len(arr)):
        left[i] = left[i - 1] + arr[i - 1]
    right = 0
    # indices = []
    indices = -1
    for i in reversed(range(len(arr))):

        if left[i] == right:
            # indices.append(i)
            indices = i
        right += arr[i]

    return indices
    # print("Equilibrium Index found at", indices)