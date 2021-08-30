# 선택 정렬
# 입력 : 리스트 l
# 출력 : void

def solution(l):
  for i in range(len(l)-1):
    min_idx = i
    for j in range(i+1, len(l)):  # i부터 시작할 필요가 없는 게 그럼 l[i] == l[i] 하는 꼴이기 때문에 i+1부터 시작
      if l[min_idx] > l[j]:
        min_idx = j # 더 작은 값을 찾았다면 min_idx를 바꿔주는 작업도 필요
    l[i], l[min_idx] = l[min_idx], l[i]
    print(l)

  print(l)

l = [2, 4, 5, 1, 3]
solution(l)
print(l)