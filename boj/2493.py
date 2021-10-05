# 09-21
# 스택을 이용하는 문제임. 브루트포스로 풀면 시간초과
import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
receives = [0 for _ in range(len(towers))]
stack = []

for i in range(n):
  if not stack:
    stack.append(i)
    continue 

  if towers[stack[-1]] > towers[i]:
    receives[i] = stack[-1] + 1
    stack.append(i)
    continue
  
  while stack and towers[stack[-1]] <= towers[i]:
    stack.pop()
  
  if stack:
    receives[i] = stack[-1] + 1
  stack.append(i)

print(*receives)