# 08-21
n = int(input())
a = list(map(int, input().split()))
table = [1] * n

# max값을 조정하는 식이 아님
for i in range(n):
  for j in range(i):
    # if a[m] < a[i]:
    if a[j] < a[i]:
      # table[i] = table[a.index(max(a[m], a[j]))]
      # m = j
      table[i] = max(table[i], 1 + table[j])
print(max(table))