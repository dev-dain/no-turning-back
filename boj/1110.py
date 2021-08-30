# 08-19
def calculate(n, cnt):
  if len(n) == 2:
    tmp = sum(map(int, n))
    cnt += 1
  else:
    tmp = int(n[0]+n[0])
    cnt += 1
  return tmp, cnt

n = map(int, input())
cnt = 0
tmp, cnt = calculate(n, cnt)

while tmp != n:
  tmp, cnt = calculate(tmp, cnt)
print(cnt)