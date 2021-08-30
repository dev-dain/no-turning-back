# 08-27
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  first_row = list(map(int, input().split()))
  second_row = list(map(int, input().split()))

  if n == 1:
    print(max(first_row, second_row)[0])
    continue

  dp = [[0 for _ in range(n+1)] for _ in range(3)]
  dp[1][1] = first_row[0]
  dp[2][1] = second_row[0]
  # dp[1][2] = max(dp[2][1] + first_row[1], dp[1][1])
  # dp[2][2] = max(dp[1][1] + second_row[1], dp[1][2])

  # 그 줄의 일은 그 줄에서 끝내야 한다
  for i in range(2, n+1):
    dp[1][i] = max(dp[2][i-2], dp[2][i-1])  + first_row[i-1]
    dp[2][i] = max(dp[1][i-2], dp[1][i-1]) + second_row[i-1]
  
  print(max(dp[1][n], dp[2][n]))