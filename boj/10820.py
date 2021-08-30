# 08-22
try:
  while True:
    s = list(input())
    if not s:
      raise EOFError
    s = map(ord, s)

    l = [0 for _ in range(4)]
    for c in s:
      if c == 32:
        l[3] += 1
      elif 97 <= c <= 122:
        l[0] += 1
      elif 65 <= c <= 90:
        l[1] += 1
      else:
        l[2] += 1

    for e in l:
      print(e, end=' ')
    print()
except EOFError:
  pass