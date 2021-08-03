# 이분 탐색
# 입력 : 리스트 l, 찾는 값 x
# 출력 : 찾은 값의 정수 인덱스 n, 실패 시 -1
# 재귀 함수를 통해 풀어보자

def solution(l, x, start, end):
  # if len(l) <= 0: return -1 # 언제나 리스트 원본을 넘길 것이므로 len으로 하면 안 됨
  if start > end: return -1 # 남은 탐색 범위가 없으면 종료
  mid = (start + end) // 2

  if l[mid] == x: return mid
  elif l[mid] > x: return solution(l, x, start, mid-1)
  else: return solution(l, x, mid+1, end)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(solution(d, 36, 0, 9))
print(solution(d, 5, 0, 9))