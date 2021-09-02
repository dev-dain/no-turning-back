# 09-02
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n+1)
dp[0] = dp[1] = arr[0]
for i in range(2, n+1):
  dp[i] = max(dp[i-1], 0) + arr[i-1]
  # if dp[i-1] > 0:
  #   dp[i] = dp[i-1] + arr[i-1]
  # else:
  #   idx = i
  #   dp[i] = arr[i-1]
print(max(dp))