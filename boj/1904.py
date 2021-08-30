# 08-24
# 메모리 초과, 시간 초과에 주의
def solution(n):
  if n == 1: return 1
  dp = [1] * (n+1)
  dp[2] = 2
  for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
  return dp[n]

n = int(input())
print(solution(n))