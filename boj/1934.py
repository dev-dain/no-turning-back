# 08-31
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  x, y = max(a, b), min(a, b)
  while y:
    res = x % y
    x = y
    y = res
  # 최소공배수 (a * b) / gcd(a, b)
  print((a * b) // x)