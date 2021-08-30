# 08-15
# 스택 구현
# 시간초과로 입력가속화...
import sys
input = sys.stdin.readline

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, x):
    self.stack.append(x)

  def pop(self):
    if not self.empty():
      return self.stack.pop()
    else:
      return -1
  
  def size(self):
    return len(self.stack)

  def empty(self):
    return 0 if self.stack else 1

  def top(self):
    if not self.empty():
      return self.stack[-1]
    else:
      return -1


n = int(input())
orders = [input().split() for _ in range(n)]
stack = Stack()
for order in orders:
  if len(order) != 1:
    stack.push(int(order[1]))
    continue
  print(getattr(stack, order[0])())