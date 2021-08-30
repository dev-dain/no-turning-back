# 08-20
score = []
for _ in range(5):
  s = int(input())
  if s < 40: 
    s = 40
  score.append(s)
print(sum(score) // len(score))
