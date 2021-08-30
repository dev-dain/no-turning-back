# 소수 판별 알고리즘
# 입력 : n (int)
# 출력 : boolean

def is_prime(n):
  i = 2
  while i * i <= n: # 루트 n까지만 체크
    if n % i == 0: return False
    i += 1
  return True