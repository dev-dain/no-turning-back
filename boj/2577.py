# 08-19
lst = [int(input()) for _ in range(3)]
result = str(lst[0] * lst[1] * lst[2])
arr = [0] * 10
for c in result:
  arr[int(c)] += 1
for e in arr:
  print(e)