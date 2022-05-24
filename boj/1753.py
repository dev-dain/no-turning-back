import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
  qu = []
  dist[start] = 0
  heapq.heappush(qu, (0, start))

  while qu:
    cur_dist, node = heapq.heappop(qu)
    if cur_dist > dist[node]:
      continue
    for adj_dist, adj_node in graph[node]:
      cost = cur_dist + adj_dist
      if cost < dist[adj_node]:
        dist[adj_node] = cost
        heapq.heappush(qu, (cost, adj_node))

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]    # 아놔 그래프도 리스트로 바꿔버려야겠다 그냥
dist = [sys.maxsize for _ in range(V+1)]    # 굳이 dist까지 리스트로 만들 필요 없음

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((w, v))   # 그래프에도 (거리, 노드) 순으로 저장

dijkstra(start)
for i in range(1, V+1):
  print('INF' if dist[i] == sys.maxsize else dist[i])