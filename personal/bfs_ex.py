# BFS (정석) 큐 이용
from collections import deque

# bfs에는 큐를 쓴다. 또한 재귀를 못함
# visited가 꼭 있어야 함. 
def solution(g, start):
  qu = deque([start]) # 아예 넣으면서 시작 가능
  visited = []  # 방문했는지 아닌지 보기

  while qu:
    el = qu.popleft()
    print(el)
    if el not in visited:
      visited.append(el)
      qu.extend(g[el])  # 자식 노드 리스트를 한번에 붙여버림
  
  return visited


graph = {
  1: [2, 3],
  2: [4, 5],
  3: [],
  4: [],
  5: []
}

print(solution(graph, 1))