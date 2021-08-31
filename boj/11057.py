# 08-31
n = int(input())
if n == 1:
  print(10)
else:
  dp = [[0 for _ in range(10)] for _ in range(n+1)]
  dp[1] = [1] * 10
  dp[2] = [x for x in range(10)]
  for i in range(3, n+1):
    for j in range(10):
      dp[i][j] = sum(dp[i-1][:j+1])
  res = 0
  for i in range(1, n+1):
    res += sum(dp[i])
  print(res % 10007)