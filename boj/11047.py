# 08-29
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
r = k
cnt = 0

while r > 0:
  for coin in coins:
    if r >= coin:
      cnt += r // coin
      r %= coin
      break
print(cnt)