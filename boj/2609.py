# 08-12
def gcd(x, y): 
  return x if y == 0 else gcd(y, x%y)
x, y = map(int, input().split())
print('{}\n{}'.format(gcd(x, y), int(x*y/gcd(x,y))))