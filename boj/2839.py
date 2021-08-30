# 08-21
# 그리디인가?
# 더 쉽게 풀 수 있는 방법. 5의 배수라면 무조건 5로 나눈 값이 최소값이다
def solution(n):
  if n == 3 or n == 5: return 1
  if n == 4: return -1
  table = [-1] * (n+1)
  table[3] = 1
  table[5] = 1
  for i in range(6, n+1):
    if table[i-3] != -1 and table[i-5] != -1:
      table[i] = min(table[i-3], table[i-5]) + 1
    elif table[i-3] == -1 and table[i-5] == -1:
      continue
    elif table[i-3] == -1:
      table[i] = table[i-5] + 1
    else:
      table[i] = table[i-3] + 1
  return table[n]

n = int(input())
print(solution(n))