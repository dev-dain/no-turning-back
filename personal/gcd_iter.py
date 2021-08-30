# 최대공약수 구하기
# 입력 : int, int
# 출력 : int

def gcd(a, b):
  for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
      return i