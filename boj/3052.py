# 08-19
from collections import Counter
lst = Counter([int(input()) % 42 for _ in range(10)])
print(len(lst))
