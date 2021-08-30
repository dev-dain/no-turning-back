# 08-21
# 그리디
n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))
cnt = end = 0
for i in range(len(times)):
  # 이전 회의의 끝나는 시간이 시작 시간보다 늦다면
  if end > times[i][0]:
    continue
  cnt += 1
  end = times[i][1]
print(cnt)