# 08-30
n = int(input())
wine = [int(input()) for _ in range(n)]
if n <= 2:
  print(sum(wine))
else:
  dp = [0] * (n+1)
  dp[1] = wine[0]
  dp[2] = wine[0] + wine[1]
  for i in range(3, n+1):
    dp[i] = max(dp[i-2], max(dp[:i-2]) + wine[i-2]) + wine[i-1]
  print(max(dp))