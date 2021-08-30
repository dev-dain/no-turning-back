# 08-18

t = int(input())
for _ in range(t):
  st = []
  s = input()
  for c in s:
    if c == '(':
      st.append(c)
    else:
      if len(st) == 0 or st[-1] == ')':
        print('NO')
        break
      st.pop()
  else:
    print('NO') if st else print('YES')