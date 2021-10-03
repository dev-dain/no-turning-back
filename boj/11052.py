# 10-03
n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
# for문 한 번만으로는 풀 수 없는 문제..
# 미쳤군
for i in range(1, n+1):
  dp[i] = cards[i]
  for j in range(1, i+1):
    dp[i] = max(dp[i], cards[j]+dp[i-j])
print(dp[n])