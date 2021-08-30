# 08-17
# 입출력
# EOF를 보고 알아야 하는 건가?! 미친 문제군..
# 결국 ValueError가 생기는지 아닌지 알아야 하기 때문에 try-except해야
while True:
  try:
    a, b = map(int, input().split())
    print(a+b)
  except:
    break