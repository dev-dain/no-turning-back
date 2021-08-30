# 08-20
# n % 2 == 0 이게 되다니 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
def solution(n):
  if n == 1: return 0
  if n == 2: return 1

  lst = [-1 for _ in range(n+1)]
  lst[1] = 0
  lst[2] = 1
  lst[3] = 0
  # [i-1], [i-3] 둘 모두 1이어야 이긴다!
  for i in range(4, n+1):
    lst[i] = 0 if min(lst[i-1], lst[i-3]) == 1 else 1
  
  return lst[n]

n = int(input())
print('CY') if solution(n) else print('SK')