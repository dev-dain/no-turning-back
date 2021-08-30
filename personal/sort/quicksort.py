from typing import Sequence


# 퀵소트와 동일하되 새 리스트를 반환하는 함수
def quick_sort(lst):
  if len(lst) < 2:
    return lst
  idx = len(lst) // 2 # 중앙값 사용
  pivot = lst[idx]

  left = [x for i, x in enumerate(lst) if x <= pivot and i != idx]
  right = [x for i, x in enumerate(lst) if x > pivot and i != idx]
  return quick_sort(left) + [pivot] + quick_sort(right)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
new = quick_sort(d)
print(new)