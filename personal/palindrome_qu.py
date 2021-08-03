# 팰린드롬 (회문)
# 입력 : 문자열 s
# 출력 : boolean (회문 True, 아니면 False)
# 큐와 스택 사용
from collections import deque

def solution2(s):
  qu = deque([])
  stack = []

  for c in s:
    if c.isalpha():
      qu.append(c.lower())
      stack.append(c.lower())

  while qu:
    if qu.popleft() != stack.pop(): return False
  return True