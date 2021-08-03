# n번째 피보나치 수 구하기
# 입력 : 구하고 싶은 순서 n (int)
# 출력 : n번째 피보나치 수 (int)

def fib(n):
  return 1 if n <= 2 else fib(n-1) + fib(n-2)

print(fib(10))