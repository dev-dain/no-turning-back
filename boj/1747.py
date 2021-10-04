# 10-05
# 수가 하나만 들어오기 때문에 에라토스테네스의 체보다
# 그때그때 팰린드롬이면 소수인지 판별하는 것이 더 이득
n = int(input())
sieve = [0, 0] + [1 for _ in range(1003002)]
for i in range(2, n+1):
  if sieve:
    for j in range(i+i, 1003002, i):
      sieve[j] = 0
for i in range(n, 1003002):
  if str(i) == str(i)[::-1] and sieve[i]:
    print(i)
    break