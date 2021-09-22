# 09-22
# 파이썬에서 gcd를 제공해주기 때문에 이걸 쓰면 됨
from math import gcd, sqrt
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

# 숫자들 간 나머지(R)를 없애기 위해 n[i] - n[i-1] 구해주기
# ex) A = M(최대공약수) * a + R
# B = M * b + R
# C = M * c + R
# R을 빼주면.. A - B = M * (a-b). 즉, a-b는 A-B의 약수
diff = [arr[i] - arr[i-1] for i in range(1, n)]

# 최종 gcd를 구해보자
# 한꺼번에 구할 수는 없으니까 하나씩
prev = diff[0]
for i in range(1, len(diff)):
  prev = gcd(prev, diff[i])
  # prev는 테스트케이스에서 28, 4 / 9, 3, 3, 3이 된다

divisor = set()
# 이제 구한 최대공약수의 약수들을 구하기
for i in range(2, int(sqrt(prev)) + 1):
  if prev % i == 0:
    divisor.update({i, prev//i})
divisor.add(prev)  # 최대공약수 자신도 넣어주기
divisor = list(divisor)
divisor.sort()
print(*divisor)

# 이 짓을 하면 답도 틀리고 느리다
# 여러 수의 최대공약수를 구해 약수를 구해야 하는 건 아는데
# 도대체 어떻게?
# for i in range(2, arr[0]+1):
#   tmp = arr[0] % i
#   for x in range(1, len(arr)):
#     if arr[x] % i != tmp:
#       break
#   else:
#     print(i, end=' ')