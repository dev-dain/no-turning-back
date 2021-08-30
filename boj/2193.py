# 08-19
def solution(n):
  if n <= 2: return 1
  lst = [0] * (n+1)
  # 애초부터 1로 초기화하면 된다 사실
  lst[1] = lst[2] =  1
  for i in range(3, n+1):
    lst[i] = lst[i-1] + lst[i-2]
  return lst[n]

n = int(input())
print(solution(n))