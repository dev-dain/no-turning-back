# 버블 정렬
# 입력 : 리스트 l
# 출력 : void

def solution(l):
  for i in range(len(l)-1):
    for j in range(len(l)-1-i):
      if l[j] > l[j+1]:
        l[j], l[j+1] = l[j+1], l[j]
    print(l)

d = [10, 2, 3, 4, 1, 7, 0]
solution(d)
print(d)