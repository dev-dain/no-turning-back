# 08-23
def solution(n):
  if n == 1: return 0
  table = [1 for _ in range(n+1)]

  # if-else가 아니라 개별 if로 해야 함
  for i in range(4, n+1):
    # 일단 2/3 나누기가 안될 때를 대비해서...
    table[i] = table[i-1] + 1
    if i % 3 == 0:
      table[i] = min(table[i//3] + 1, table[i])
    if i % 2 == 0:
      table[i] = min(table[i//2] + 1, table[i])

  return table[n]

n = int(input())
print(solution(n))