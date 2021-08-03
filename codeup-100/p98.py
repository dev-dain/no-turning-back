lst = []
for _ in range(10):
  lst.append(list(map(int, input().split())))
x, y = 1, 1
while True:
  try:
    if lst[y][x] == 2:
      lst[y][x] = 9
      break
    lst[y][x] = 9
    if lst[y][x+1] == 0 or lst[y][x+1] == 2:
      x += 1
    else:
      if lst[y+1][x] == 1:
        break
      y += 1
  except IndexError:
    break
  
for e in lst:
  for c in e:
    print(c, end=' ')
  print()