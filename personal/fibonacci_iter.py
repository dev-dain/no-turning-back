# n번째 피보나치 수 구하기 (반복문)
# 입력 : n (정수)
# 출력 : n번째 피보나치 수

def solution(n):
  if n <= 1: return n
  x = 1
  y = 1
  res = 0
  for _ in range(n):
    x = y
    y = res
    res = x + y
  return res

print(solution(10))