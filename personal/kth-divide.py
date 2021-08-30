# 08-17
# K번째 약수

# count를 쓰는 방법도 있음
n, k = map(int, input().split())
lst = [i for i in range(1, n//2+1) if n % i == 0]
lst.append(n)
if len(lst) < k:
  print(-1)
else:
  print(lst[k-1])