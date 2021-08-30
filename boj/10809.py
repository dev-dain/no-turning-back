# 08-21
from collections import defaultdict
import string

s = input()
counter = defaultdict(lambda:-1)
for i, c in enumerate(s):
  if counter[c] == -1:
    counter[c] = i

for c in string.ascii_lowercase:
  print(counter[c], end=' ')