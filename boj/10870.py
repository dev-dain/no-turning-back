def fib(n):
  if n <= 1: return n
  x, y = 0, 1
  for _ in range(n):
    x, y = y, x + y
  return x

n = int(input())
print(fib(n))