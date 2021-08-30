# 08-16
c = int(input())

for _ in range(c):
  n, *arr = map(int, input().split())
  avg = sum(arr) / len(arr)
  avg_arr = [n for n in arr if n > avg]
  print('{:.3f}%'.format(len(avg_arr) / len(arr) * 100))
