# 08-21
a, b, c = map(int, input().split())

# 시간초과 이유는 아주 큰 수이기 때문
# 매번 연산할 때마다 c 모듈러 연산 필요
def solution(a, b):
  if b == 1: return a % c
  if b % 2 == 0: return solution(a, b//2) ** 2 % c
  if b % 1 == 0: return solution(a, b//2) ** 2 * a % c

print(solution(a, b) % c)