# 08-19
# 병합정렬, 힙 정렬보다 그냥 내장 sort가 빠르다.. 허무하군 ㅋㅋ
import sys
input = sys.stdin.readline
import heapq

# def merge_sort(lst):
#   if len(lst) == 1: return

#   mid = len(lst) // 2  
#   g1 = lst[:mid]
#   g2 = lst[mid:]
#   merge_sort(g1)
#   merge_sort(g2)
  
#   idx = 0
#   while g1 and g2:
#     if g1 < g2:
#       lst[idx] = g1.pop(0)
#     else:
#       lst[idx] = g2.pop(0)
#     idx += 1
  
#   while g1:
#     lst[idx] = g1.pop(0)
#     idx += 1
#   while g2:
#     lst[idx] = g2.pop(0)
#     idx += 1

# 힙 알아보기 (heapq.heappush 하는 것)
n = int(input())
lst = []
for _ in range(n):
  heapq.heappush(lst, int(input()))

while lst:
  print(heapq.heappop(lst))
# merge_sort(lst)
