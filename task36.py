def palindrom(a):
    if len(a) <= 1:
        return True
    if a[0] == a[-1]:
        return palindrom(a[1:-1])
    else:
        return False
a = 'потоп'
print(palindrom(a))    