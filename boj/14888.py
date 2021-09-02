# 09-02
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
pl, mi, mul, div = map(int, input().split())
operator = '{}{}{}{}'.format(pl * '+', mi * '-', mul * '*', div * '/')
res = []

for combi in set(permutations(operator)):
  st = [e for e in a[::-1]]

  for i in range(n-1):
    x = st.pop()
    y = st.pop()
    if combi[i] == '/':
      st.append(x // y) if x > 0 else st.append(-(-x // y))
    else:
      st.append(eval(f'{x}{combi[i]}{y}'))

  res.append(st[0])

print(max(res))
print(min(res))