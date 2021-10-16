# 10-16
pieces = list(map(int, input().split()))
for i in range(len(pieces)-1):
  for j in range(1, len(pieces)):
    if pieces[j-1] > pieces[j]:
      pieces[j-1], pieces[j] = pieces[j], pieces[j-1]
      print(*pieces)