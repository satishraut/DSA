def towerofHanoi(n, source, aux, dest):
    if n == 0:
        return

    towerofHanoi(n - 1, source, dest, aux)
    print(source, dest)
    towerofHanoi(n - 1, aux, source, dest)


n = int(input())
towerofHanoi(n, 'a', 'b', 'c')

