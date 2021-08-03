# 최댓값을 재귀로 구하는 시도
# 입력 : n개 숫자 리스트
# 출력 : 최댓값 n

def solution(lst):
  if len(lst) == 1:
    return lst[0]
  candidate = solution(lst[1:])
  return lst[0] if candidate < lst[0] else candidate

print(solution([1, 5, 3, 2, 16, 4, 5, 6, 9, 5, 3]))