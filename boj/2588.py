# 08-19
a = int(input())
b = input()
lst = [a * int(b[i]) for i in range(len(b)-1, -1, -1)]
lst.append(a * int(b))
for e in lst:
  print(e)