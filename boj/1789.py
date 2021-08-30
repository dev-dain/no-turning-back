# 08-14
s = int(input())
root = int(pow(s*2, 1/2))
n = (root * (root + 1)) // 2
while n > s:
  n = (root * (root - 1) // 2)
  root -= 1
print(root)