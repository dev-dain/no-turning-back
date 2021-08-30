# 08-16
def paper_func(paper):
  if len(paper) == 1:
    return (1, 0) if paper[0][0] == 1 else (0, 1)

  lst = []
  state = paper[0][0]

  for row in range(len(paper)):
    for block in range(len(row)):
      if paper[row][block] != state:
        mid = len(paper[0]) // 2
        lst.append(paper_func(paper[:mid][:mid]))
        return lst
  else:
    return (1, 0) if state == 1 else (0, 1)

p = [[0, 0], [0, 0]]
print(len(p))

p = (1, 0)
p2 = (0, 1)
print(sum(zip(p, p2)))
print(p+p2)