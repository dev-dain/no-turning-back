# 08-12
# combinations를 사용해 구현하는 방법도 있으니 참고!
from bisect import bisect
def dp_longest_subseq(lst):
  l = [1] * len(lst)

  for idx, val in enumerate(lst):
    for pre in range(idx):  # 그니까.. 내부 루프가 0부터 len(lst)-1만큼 점차 커지면서 도는 거
      if lst[pre] <= val: # 이전 인덱스의 값보다 지금 값이 더 크다면
        l[idx] = max(l[idx], 1 + l[pre])  # 현재 인덱스 값과 1 + 이전 인덱스 l 값을 비교해 큰 값 대입. max 주목!
        print('{}:{}'.format(pre, 1 + l[pre], end=' '))
    print()

  return max(l)


def bi_longest_subseq(lst):
  end = []
  for val in lst:
    idx = bisect(end, val)
    if idx == len(end):
      end.append(val)
    else:
      end[idx] = val  # 어차피 덮어쓰니까 괜찮음
    print(idx)
  return len(end)

s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]
# print(dp_longest_subseq(s1))
print(bi_longest_subseq(s1))