# 08-19
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
cards = Counter(sorted([int(input()) for _ in range(n)]))
# cards = Counter(sorted(cards))
print(cards.most_common(1)[0][0])
# 왜 틀린건데 도대체..
# Counter로 감싼 게 문제였는데 왜 문제인지 모르겠네..

