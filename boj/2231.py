# 08-25
n = int(input())
l = len(str(n))
for i in range(n-(l*9), n):
  # -일 때를 고려해줘야
  divide_i = sum([int(c) for c in str(i) if c != '-'])
  if i + divide_i == n:
    print(i)
    break
else:
  print(0)