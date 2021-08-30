# 08-19
n = int(input())
p = sorted(map(int, input().split()))
print(sum([sum(p[:i]) for i in range(1, len(p)+1)]))
