# 08-18
# 입출력
# EOF 에러를 사용해야 함 (언제 끝날지 모르면)
while True:
  try:
    s = input()
    print(s)
  except EOFError:
    break