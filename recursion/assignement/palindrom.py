def checkPalin(st, si, ei):
    if len(st) == 1 or len(st) == 0:
        return True
    if st[0] != st[-1]:
        return False
    smalloutput = checkPalin(st[1:-1], si + 1, ei - 1)
    if smalloutput:
        return True
    return False


st = input()
if (checkPalin(st, 0, len(st))):
    print("true")
else:
    print("false")