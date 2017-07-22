def backstr(s):
    n = len(s)
    k = ''
    while s != '':
        k = s[0:2]+k
        s=s[2:]
    return k


print backstr('1234567890k')
