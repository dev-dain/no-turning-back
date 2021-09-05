# 09-05
import math, bisect, sys
input = sys.stdin.readline

prime = [False, False, True] + ([True] * 1000000)
for i in range(2, int(math.sqrt(len(prime)))+1):
  if prime[i]:
    for j in range(i * 2, len(prime), i):
      prime[j] = False
prime = [i for (i, x) in enumerate(prime) if x]

while True:
  n = int(input())
  if n == 0:
    break
  p1 = 0
  p2 = bisect.bisect(prime, n)-1
  flag = False
  while p1 <= p2:
    if prime[p1] + prime[p2] == n:
      print(f'{n} = {prime[p1]} + {prime[p2]}')
      flag = True
      break
    elif prime[p1] + prime[p2] < n:
      # p1 = (p1 + p2) // 2
      p1 += 1
    else:
      p2 -= 1
      # p2 = (p1 + p2) // 2
  if not flag:
    print("Goldbach's conjecture is wrong.")