# 08-19
n = int(input())
lst = list(set([input() for _ in range(n)]))
lst.sort(key=lambda x: (len(x), x))
for word in lst:
  print(word)