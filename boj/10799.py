# 08-24
import sys
input = sys.stdin.readline

s = input()
stack = []
cnt = 0
for i in range(len(s)):
  if s[i] == '(':
    stack.append(s[i])
  else:
    if s[i-1] == '(':
      # 레이저
      stack.pop()
      cnt += len(stack)
    else:
      # 쇠막대의 끝
      if stack:
        stack.pop()
      cnt += 1

print(cnt-1)