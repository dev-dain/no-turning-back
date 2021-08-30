# 08-12

l = [sorted(list(map(int, input().split()))) for _ in range(int(input()))]
for m in l: print(m[-3])