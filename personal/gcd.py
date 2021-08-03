# 최대공약수 구하기
# 입력 : 두 수 x, y
# 출력 : x, y의 최대공약수

def gcd(x, y):
  return x if y == 0 else gcd(y, x%y) 

print(gcd(21, 12))