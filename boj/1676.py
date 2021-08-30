# 08-25, 08-27
# 와 전혀 다른 방식이네.. 신선하다
# 그니까 재귀로 500까지 팩토리얼을 구하면 너무 비효율적이니까
# 주어진 수에 2*5가 얼마나 있는지 구하라는거네.. 와..
n = int(input())
five_arr = [x for x in range(5, n+1, 5)]
cnt = 0
for five in five_arr:
  while five % 5 == 0:
    five //= 5
    cnt += 1
print(cnt)