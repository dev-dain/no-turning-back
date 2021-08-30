# 08-05
# https://programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호

def solution(s):
    if s == '' or s[0] == ')': return False
    st = []
    for c in s:
        if c == '(': st.append(c)
        else:
            if len(st) == 0: return False
            st.pop()
    if len(st) == 0: return True
    return False