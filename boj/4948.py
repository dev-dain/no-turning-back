# 08-23
import math

# 시간초과
# 아님 에라토스테네스의 체?
# 헐... math import 안 하고 **1/2 하니까 시간초과구나 ㅋㅋ
# 아예 lst[i]가 True이면 2중 루프를 그 때 돌도록 할 수 있음
# for j in range(2*i, len(lst), i) 이렇게.. 그 때는 일괄로 False로 만들어버리면 됨
lst = [1 for _ in range(123456*2+1)]
for i in range(2, len(lst)):
  for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
      lst[i] = False
      break

# def get_count(n):
#   global lst
#   return lst[n]

while True:
  n = int(input())
  if n == 0: break
  if n == 1: 
    print(1)
    continue

  print(sum([lst[x] for x in range(n+1, 2*n+1)]))    

  # if len(lst) >= (n*2+1):
    # 만약 리스트가 더 길다면 그냥 있는 걸로 계산
    # print(list(filter()))
  # else:
    # 아니면 리스트 새로 만들기
    # new_lst = [0 for _ in range(n*2+1-len(lst))]
  # for i in range(n+1, n*2+1):
  #   for j in range(2, int(i**1/2)):
  #     if i % j == 0: