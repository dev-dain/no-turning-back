# 08-24
from collections import deque

n, m = map(int, input().split())
q = deque(range(1, n+1))
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
  if q[0] == num:
    q.popleft()
  else:
    # 시작하는 위치는 고정되어 있고 찾을 수의 위치가 문제
    idx = q.index(num)
    while q[0] != num:
      if idx > len(q) // 2:
        q.rotate(1)
      else:
        q.rotate(-1)
      cnt += 1
    q.popleft()

print(cnt)