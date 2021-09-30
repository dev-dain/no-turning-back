# 09-30
import bisect
fib = [0, 1]
while fib[-1] < 1000000000:
  fib.append(fib[-2]+fib[-1])
fib.pop()

t = int(input())
for _ in range(t):
  n = int(input())
  idx = bisect.bisect(fib, n) - 1
  res = n-fib[idx]
  arr = [fib[idx]]
  while res > 0:
    idx = bisect.bisect(fib, res) - 1
    res -= fib[idx]
    arr.append(fib[idx])
  arr.sort()
  print(*arr)