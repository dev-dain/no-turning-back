# 08-25
n = list(map(lambda x: int(x), input()))
n.sort(key=lambda x: -x)
n = list(map(str, n))
print(''.join(n))