# 09-01
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  s = [0] + list(map(int, input().split()))
  visited = [0] * (n+1)

  for i in range(1, n+1):
    # 아직 팀이 없는 학생이라면..
    if visited[i] == 0:
      team = i
      while visited[i] == 0:
        # 팀 구성해줌
        visited[i] = team
        # 이제 i는 i번째 학생이 선택한 학생 번호가 됨
        i = s[i]
        # 사이클이 있다면 사이클 시작 부분부터 사이클 끝까지 
        # 다시 순환하며 -1 체크 (팀이 됨)
      while visited[i] == team:
        visited[i] = -1
        i = s[i]

  print(n - visited.count(-1))