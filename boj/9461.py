# 08-25
t = int(input())
dp = [0, 1, 1, 1]

for _ in range(t):
  n = int(input())

  # 그냥 < 이면 4일 때 IndexError 발생
  if len(dp) <= n:
    org_len = len(dp)
    dp.extend([0 for _ in range(n-len(dp)+1)])
    for i in range(org_len, n+1):
      dp[i] = dp[i-2] + dp[i-3]
  
  print(dp[n])