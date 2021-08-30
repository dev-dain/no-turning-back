# 데크
from collections import deque

q = deque([1, 2, 3, 4, 5])
q.append(6)
print(q.popleft())
print(q)
q.appendleft(1)
print(q.pop())
print(q)
q.rotate(3) # [3, 4, 5, 1, 2] 오른쪽 시프트
print(q)
q.rotate(-2)  # [5, 1, 2, 3, 4]
print(q)