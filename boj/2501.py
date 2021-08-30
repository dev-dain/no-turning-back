# n번째로 작은 약수 구하기
# https://www.acmicpc.net/problem/2501
# 입력 : int, int
# 출력 : int

n, k = map(int, input().split())
l = [1]
for i in range(2, (n//2)+1):
  if bool(n % i): continue
  l.append(i)
  if len(l) == k: break
l.append(n)

try: print(l[k-1])
except: print(0)