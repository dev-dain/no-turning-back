# 힙 정렬
import heapq

def heap_sort(lst):
  h = []
  for val in lst:
    heapq.heappush(h, val)
  return [heapq.heappop(h) for _ in range(len(h))]

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
new = heap_sort(d)
print(new)