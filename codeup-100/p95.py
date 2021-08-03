l = [[0 for i in range(19)] for j in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    l[x-1][y-1] = 1
for x in l:
    for y in x:
        print(y, end=' ')
    print()