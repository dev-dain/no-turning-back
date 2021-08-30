# 스택
class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if self.isEmpty():
      return '스택이 비었습니다.'
    return self.stack.pop()
  
  def peek(self):
    if self.isEmpty():
      return '스택이 비었습니다.'
    return self.stack[-1]

  def isEmpty(self):
    return not bool(self.stack)
  
  def size(self):
    return len(self.stack)

  def __repr__(self):
    return repr(self.stack)


if __name__ == '__main__':
  stack = Stack()
  print('스택이 비었나요? {}'.format(stack.isEmpty()))
  for i in range(5):
    stack.push(i)
  print(stack)
  print(stack.size())
  print(stack.peek())
  for i in range(1, 5):
    print(stack.pop())
  print(stack.pop())