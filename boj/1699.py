# 09-06
n = int(input())
if n < 4:
  print(n)
else:
  dp = [0] * (n+1)
  # 아예 square 배열을 만들어버림
  square = [i * i for i in range(1, 317)]

  for i in range(1, n+1):
    s = []
    # 제곱수를 돌려서 제곱수가 더 커질 때까지 일단 넣고 봄
    for j in square:
      if j > i: break
      # 제곱수가 i와 같거나 작다면 
      s.append(dp[i-j])
    dp[i] = min(s) + 1
  print(dp[n])