# 09-03
var, *s = input().split()
s = list(map(lambda x : x.strip(',').strip(';'), s))
for x in s:
  new_var = var
  bracket = {'[': ']', ']': '['}
  rev = ''.join([bracket.get(c) if c in '[]' else c for c in x[::-1] if c in '&[]*'])
  name = ''.join([c for c in x if c not in '&[]*'])
  print(f'{new_var}{rev} {name};')