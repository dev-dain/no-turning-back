# 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘

# 입력 : 리스트 l과 찾는 정수 n
# 출력 : n이 있는 위치를 담은 list

def solution(l, n):
  lst = []
  for i in range(len(l)):
    if l[i] != n:
      continue
    lst.append(i)
  return lst

print(solution([5, 3, 2, 4, 5, 5, 1, 6, 3, 4], 4))
print(solution([5, 3, 2, 4, 5, 5, 1, 6, 3, 4], 8))
