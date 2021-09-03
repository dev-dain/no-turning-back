# 09-03
e, s, m = map(int, input().split())

if e == 1 and s == m:
  print(s)
else:
  i = min(e, s, m)
  add = 0
  if min(e, s, m) == e: add = 15
  elif min(e, s, m) == s: add = 28
  else: add = 19

  if e == 15: e = 0
  if s == 28: s = 0
  if m == 19: m = 0
  
  while True:
    if i % 15 == e and i % 28 == s and i % 19 == m:
      break
    i += add
  print(i)