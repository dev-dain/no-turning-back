# 08-15
n = int(input())
l = [int(input()) for _ in range(n)]

for i in range(1, len(l)):
  key = l[i]
  j = i - 1
  
  while j >= 0 and l[j] > key:
    l[j+1] = l[j]
    j -= 1
  
  l[j+1] = key  # j+1을 잊지 말 것

for e in l:
  print(e)
'''
for i in range(len(l)):
  min_idx = i
  for j in range(i+1, len(l)):
    if l[min_idx] > l[j]:
      min_idx = j
  l[min_idx], l[i] = l[i], l[min_idx]
'''
'''
for i in range(len(l)-1):
  for j in range(i+1, len(l)):
    if l[i] > l[j]:
      l[i], l[j] = l[j], l[i]
'''

print(l)