# 08-20
import heapq, sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
  x = int(input())
  if x == 0:
    print(heapq.heappop(lst)[1]) if lst else print(0)
  else:
    # 최대 힙을 만들 때는 그냥 값을 집어넣지 말고 튜플로 우선순위를 만들어 집어넣음
    # 이 때 우선순위는 음수로...
    heapq.heappush(lst, (-x, x))
