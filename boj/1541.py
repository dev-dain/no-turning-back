# 09-27 (아.. 괄호를 한 개만 치는 문제가 아니구나)
# -를 기준으로 쪼개기
s = input().split('-')
result = 0
# 첫 번째 빼기 기준 왼쪽 항에 +가 있다면
# 즉 덧셈식이 있다면 더한다
# 덧셈식이 없더라도 첫 항은 더함
for i in s[0].split('+'):
  result += int(i)
# 그 뒤부터는...
for i in s[1:]:
  # 덧셈식이 있다면 앞뒤로 쭉 빼주고 
  # 덧셈식이 없더라도 그냥 빼준다 (괄호를 치는 것)
  for j in i.split('+'):  
    result -= int(j)
print(result)

'''
55 50+40
50+50 -(100+100) 100 100
50+50-100+100-100-100
'''