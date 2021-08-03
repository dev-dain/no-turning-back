# 진법 변환
# 입력 : n진법으로 나타낸 숫자 n과 base
# 출력 : 10진법으로 나타낸 숫자 n

def solution(n, base):
  n_list = [c for c in str(n)]
  n_list.reverse()
  result = 0
  for i in range(len(n_list)):
    result += int(n_list[i]) * (base ** i)

  return result

print(solution(1100, 8))