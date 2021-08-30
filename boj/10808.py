# 08-20
from collections import Counter
import string

s = Counter(input())
for c in string.ascii_lowercase:
  print(s.get(c), end=' ') if s.get(c) else print(0, end=' ')
