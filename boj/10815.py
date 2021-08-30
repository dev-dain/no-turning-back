# 08-19
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
cards = Counter(map(int, input().split()))
m = int(input())
needs = map(int, input().split())
result = [1 if cards.get(need) else 0 for need in needs]
for val in result:
  print(val, end=' ')