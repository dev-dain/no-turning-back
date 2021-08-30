# 08-19

t = int(input())

for _ in range(t):
  n = int(input())
  if n <= 2:
    print(n)
    continue

  lst = [0 for _ in range(n+1)]
  lst[1] = 1
  lst[2] = 2
  lst[3] = 4

  for i in range(4, n+1):
    lst[i] = lst[i-1] + lst[i-2] + lst[i-3]

  print(lst[n])