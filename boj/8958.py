# 08-19
t = int(input())
for _ in range(t):
  s = input()
  o = [i for i in range(len(s)) if s[i] == 'O']
  sum = seq = 0

  for i in range(len(o)):
    if o[i] - o[i-1] == 1:
      seq += 1
      sum += 1 + seq 
    else:
      seq = 0
      sum += 1

  print(sum)