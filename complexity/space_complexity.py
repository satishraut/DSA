from sys import stdin


def intersection(a, b, n, m):
    # Your code goes here
    i = 0
    j = 0
    a.sort()
    b.sort()

    while (i < n and j < m):

        if (a[i] > b[j]):
            j += 1

        else:
            if (b[j] > a[i]):
                i += 1

            else:
                # when both are equal
                print(a[i], end=" ")
                i += 1
                j += 1