s = input()
st = []
sum = 0
for i in range(len(s)):
  if s[i] == '(':
    st.append(s[i])
  # 레이저인 것을 어떻게 판별하는지?
  # 막대기가 끝날 때 무조건 pop할 것!
  # )는 스택에 들어가지 않는다
  else:
    st.pop()
    # 아 i-1로 검사하는구나.. 
    if s[i-1] == '(':
      sum += len(st)
    # 바로 앞이 닫는 괄호, 즉 레이저가 아니면
    # 해당 쇠막대기가 끝난 거니까 꽁다리 1 추가
    else:
      sum += 1
print(sum)