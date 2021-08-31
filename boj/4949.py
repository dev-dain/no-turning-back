# 08-25, 08-28
while True:
  s = input()
  stack = []
  if s[0] == '.':
    break
  
  for c in s:
    if c == '(' or c == '[':
      stack.append(c)
    elif c == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        print('no')
        break
    elif c == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        print('no')
        break
  # 루프가 끝나면 스택에 뭔가 남았는지도 검사해야함
  else:
    print('no') if stack else print('yes')
  