# 08-23
def solution(n):
  if n == 1: return 1
  dp = [1 for _ in range(n+1)]
  dp[2] = 3

  for i in range(3, n+1):
    # 맞네.. dp[1]은 1이니까 굳이 안 곱해줘도 되네
    # dp[2]-1도 2잖아! 젠장 ㅋㅋㅋㅋ
    dp[i] = ((dp[1] * dp[i-1]) + ((dp[2]-1) * dp[i-2])) % 10007
  return dp[n]

n = int(input())
print(solution(n))