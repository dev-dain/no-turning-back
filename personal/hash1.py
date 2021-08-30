from collections import Counter

n = int(input())
words = Counter([input() for _ in range(n)])
written = Counter([input() for _ in range(n-1)])

print((words - written).most_common(2)[0][0])
