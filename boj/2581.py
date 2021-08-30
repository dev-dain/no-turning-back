# 08-13
# a, b = [int(input()) for _ in range(2)]
# lst = [True] * b
# if len(lst) >= 1: 
#   lst[1] = False

# for i in range(2, int(b**1/2)+1):
#   if lst[i] == True:
#     for j in range(i * 2, b, i):
#       lst[j] = False

# lst = [x[0] for x in filter(lambda x : x if x[1] == True else False, enumerate(lst)) \
#       if x[0] >= a and x[0] <= b]

# if len(lst) >= 1: 
#   print('{}\n{}'.format(sum(lst), min(lst)))
# else: 
#   print(-1)


m, n = [int(input()) for _ in range(2)]
lst = []
for i in range(m, n+1):
  if i < 2: continue  # 허무하다 이거 때문에 엄청 틀림ㅋㅋㅋ
  for j in range(2, int(i**1/2)+1):
    if i % j == 0: break
  else:
    lst.append(i)

if lst: 
  print('{}\n{}'.format(sum(lst), min(lst)))
else:
  print(-1)