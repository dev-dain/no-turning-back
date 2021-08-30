# 에라토스테네스의 체 방식으로 소수를 구해보자
target = 1000 # 구하려는 값의 범위
prime_list = [True] * target
prime_list[1] = False
m = int(target ** 1/2)+1
for i in range(2, m):
  if prime_list[i] == True:
    for j in range(i * 2, target, i):
      prime_list[j] = False

print([x[0] for x in filter(lambda i : i[0] if i[1] == True else False, enumerate(prime_list))])