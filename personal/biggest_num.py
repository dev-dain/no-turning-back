# 08-17
# k만큼 숫자 삭제, 가장 큰 수 만들기

n, m = map(int, input().split())
n = list(str(n))

st = []
for c in n:
  # len(st)이 아니라 그냥 st으로
  # 그리고 while, if를 합쳐서 최적화시킬 수 있음
  while st and m:
    if int(st[-1]) < int(c):
      st.pop()
      m -= 1
    else:
      st.append(c)
      break
  if not st or not m:
    st.append(c)
    continue
# 오 여기서 뒤를 잘라버릴 수도 있네 좋은 방법이다
while m != 0:
  # st = st[:-m]
  st.pop()
  m -= 1

print(''.join(st))