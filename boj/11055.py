# 09-01
# 리뷰 필요
n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = a[0]

for i in range(2, n+1):
  for j in range(1, i):
    if a[i-1] > a[j-1]:
      dp[i] = max(dp[i], dp[j])
  dp[i] += a[i-1]
print(max(dp))