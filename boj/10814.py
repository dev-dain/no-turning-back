# 08-19
n = int(input())
lst = [input().split() for _ in range(n)]
lst.sort(key=lambda x: int(x[0]))
for age, name in lst:
  print(age, name)