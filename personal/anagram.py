# 주어진 두 문자열이 애너그램인지 확인하기
# 입력 : str, str
# 출력 : boolean
from collections import Counter

def solution(s1, s2):
  count = Counter([c for c in s1])
  count -= Counter([c for c in s2])
  for i in count.values():
    if i == 0: continue
    return False
  return True

print(solution('google', 'gougol'))
print(solution('anabel', 'lanbea'))