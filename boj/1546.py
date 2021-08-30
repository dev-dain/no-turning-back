# 08-19
n = int(input())
scores = list(map(int, input().split()))
scores = [score / max(scores) * 100 for score in scores]
print(sum(scores) / n)
