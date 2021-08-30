# 08-19
t = int(input())
q = 25
d = 10
n = 5
p = 1

for _ in range(t):
  c = int(input())
  qc = dc = nc = pc = 0

  while c >= q:
    c -= q
    qc += 1
  while c >= d:
    c -= d
    dc += 1
  while c >= n:
    c -= n
    nc += 1
  while c >= p:
    c -= p
    pc += 1
  
  print(qc, dc, nc, pc)