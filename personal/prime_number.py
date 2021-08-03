# 소수 판별 알고리즘
# 입력 : n (int)
# 출력 : boolean
import math

def is_prime(n):
  n = abs(n)  # 먼저 절댓값을 구한다
  if n < 4: return True # 4보다 작으면 무조건 소수
  root = math.sqrt(n)
  for i in range(2, math.ceil(root)):
    if n % i == 0: return False
  return True

print(is_prime(505))