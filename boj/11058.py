# 09-05
n = int(input())
if n <= 6: print(n)
else:
  dp = [0] * (n+1)
  for i in range(1, 4):
    dp[i] = i
  for i in range(4, n+1):
    dp[i] = i
    for j in range(3, i):
      dp[i] = max(dp[i], dp[i-j] * (j-1))
  print(dp[n])