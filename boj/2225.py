# 09-03
# n, k = map(int, input().split())
# if k == 1:
#   print(1)
# else:
#   dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
#   dp[1][1] = 1
#   dp[2] = [1 for _ in range(n+1)]
#   for i in range(3, k+1):
#     for j in range(n+1):
#       dp[i][j] = sum(dp[i-1]) - sum(dp[i-1][:j])
#   print(dp)
#   print(sum(dp[k]) % 1000000000)


# 다른 풀이 (이게 더 빠름)

n, k = map(int, input().split())
if k == 1:
  print(1)
else:
  dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
  dp[1] = [0] + [1 for _ in range(n)]
  dp[2] = [0] + [x+1 for x in range(1, n+1)]
  for i in range(3, k+1):
    dp[i][1] = i
    for j in range(2, n+1):
      dp[i][j] = dp[i][j-1] + dp[i-1][j]
  print(dp[k][n] % 1000000000)
  print(dp)