from collections import deque

def solution(bridge_length, weight, truck_weights):
  qu = deque(truck_weights)
  passing = []
  passing_count = []
  time = 1

  while qu:
    if not qu: 
      time += bridge_length
      break
    if weight - sum(passing) < qu[0]:
      passing.append(qu.popleft())
      time += bridge_length
      passing.pop()
      continue

    while weight - sum(passing) > qu[0]:
      # 도대체 시간이 passing에 들어온 시간과 time을 어떻게 일일이 비교한단 말인가?
      passing_count = [time]
      passing.append(qu.popleft())
      time += 1
      break

  return time

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))