# 08-26
n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(1, 10):
  dp[1][i] = 1

for i in range(2, n+1):
  for j in range(10):
    if not j:
      dp[i][j] = dp[i-1][1]
    elif j == 9:
      dp[i][j] = dp[i-1][8]
    else: 
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# 나머지 연산은 마지막에만
print(sum(dp[n]) % 1000000000)