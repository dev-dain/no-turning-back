# 08-05
# https://programmers.co.kr/learn/courses/30/lessons/72410
# 신규 아이디 추천

def solution(new_id):
    new_id = ''.join([c for c in new_id.lower() if c.isalnum() or c in '-._'])
    for i in range(len(new_id)//2):
        new_id = new_id.replace('..', '.').strip('.')
    if len(new_id) == 0: new_id = 'a'
    if len(new_id) >= 16: return new_id[:15].strip('.')
    if len(new_id) <= 2: return new_id.ljust(3, new_id[-1])
    return new_id