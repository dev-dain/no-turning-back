n = int(input())
l = map(int, input().split())
lst = [0 for i in range(23)]
for e in l:
    lst[e-1] += 1
for e in lst:
    print(e, end=' ')