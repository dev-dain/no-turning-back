# 브루트포스
# 08-15

n, m = map(int, input().split())
l = sorted(map(int, input().split()))
diff = m
for i in range(len(l)-2):
  for j in range(i+1, len(l)-1):
    for k in range(i+2, len(l)):
      if m-l[i]-l[j]-l[k] >= 0 and m-l[i]-l[j]-l[k] < diff:
        diff = m-l[i]-l[j]-l[k]
print(m-diff)

# combinations를 썼으면 더 빨랐겠구나