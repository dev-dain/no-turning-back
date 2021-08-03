# 제너레이터를 만들어 n번째까지 피보나치 수 출력하기
def fib_generator(n):
  if n <= 2: return 1

  x = y = 1
  res = x + y

  for _ in range(n):
    yield x
    x = y
    y = res
    res = x + y

fib = fib_generator(10)
for i in range(10):
  print(next(fib), end=' ')