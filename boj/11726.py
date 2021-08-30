# 08-19
def solution(n):
  if n <= 3: 
    return n
  table = [0 for _ in range(n+1)]
  table[1] = 1
  table[2] = 2
  for i in range(3, n+1):
    table[i] = (table[i-1] + table[i-2]) % 10007
  return table[n]

n = int(input())
print(solution(n))