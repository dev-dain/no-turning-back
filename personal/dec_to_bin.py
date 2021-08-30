decnum = int(input())
s = []
str_aux = ''

while decnum > 0:
  dig = decnum & 1
  decnum = decnum >> 1
  s.append(dig)

while s:
  str_aux += str(s.pop())

print(str_aux)