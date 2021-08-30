from bisect import bisect

n, m = map(int, input().split())
lst = sorted(map(int, input().split()))
# print(bisect(lst, m))

def bin_search(lst, x, start, end):
  if start > end: return -1 # 남은 탐색 범위가 없는 경우임
  mid = (start + end) // 2

  if lst[mid] == x: return mid
  # 리스트는 항상 원본 그대로를 넘긴다
  elif lst[mid] < x: return bin_search(lst, x, mid+1, end)
  else: return bin_search(lst, x, start, mid-1)

print(bin_search(lst, m, 0, n)+1)
# 반복문으로도 짜보기!