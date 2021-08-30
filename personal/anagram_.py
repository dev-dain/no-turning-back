from collections import Counter

w1 = Counter(input())
w2 = Counter(input())
print("NO") if w1-w2 else print("YES")
