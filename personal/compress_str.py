# 문자열 압축하기
# 입력 : str
# 출력 : str

def solution(s):
  lst = []
  count, last = 1, '' # 일단 count를 1로 설정
  for i, c in enumerate(s):
    if c == last:
      count += 1  
    else:
      if i != 0:  # i가 0인 경우엔 처음이니 count를 추가하지 않음
        lst.append(str(count))  # 그 다음 숫자 추가
      lst.append(c) # 일단 문자부터 추가
      last = c
      count = 1
  lst.append(str(count))  # 마지막에 남은 숫자 추가
  return ''.join(lst)

print(solution('aaabbbbbbccda'))