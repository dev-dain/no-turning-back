# 08-19
s = input()
lst = sorted([s[i:] for i in range(len(s))])
for e in lst:
  print(e)