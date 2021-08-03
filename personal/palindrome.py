# 팰린드롬 (회문)
# 입력 : 문자열 s
# 출력 : boolean (회문 True, 아니면 False)
# 문자열 비교

def solution(s):
  str_s = ''.join([c.lower() for c in s if c.isalpha()])
  return str_s == str_s[::-1]

print(solution('Hi How are you?'))
print(solution('Wow'))
print(solution("Madam, I'm Adam"))
print(solution("Madam, I am Adam"))