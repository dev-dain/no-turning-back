# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기
# 입력 : str
# 출력 : str

def solution(s):
    lst1 = [''.join([word[i].lower() if i % 2 else word[i].upper() \
                     for i in range(len(word))]) for word in s.split(' ')]
    return ' '.join(lst1)