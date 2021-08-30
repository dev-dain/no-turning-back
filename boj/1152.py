# 08-16

# split으로 앞뒤 공백을 없애주고
# whitespace도 잘라야 함
# isspace로는 못 잡네
s = input().strip()
print(len([word for word in s.split(' ') if word != '']))