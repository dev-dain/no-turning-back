# DFS (정석) 스택 이용
# dfs에는 스택을 쓴다
# visited가 꼭 있어야 함. 

# 재귀함수로 구현할 때는 visited를 헤더에 넣어줘야 함
def solution(g, start, visited = []):
  visited.append(start) # 일단 visited에 start를 넣는다. 방문했으니까

  for node in g[start]: # 자식 노드로 루프 돌리기
    if node not in visited: # 노드가 방문하지 않은 노드라면
      # 재귀를 하되 start는 현재 node로, visited는 현재까지 visited를 보내기
      # 이렇게 하면 하나의 leaf node까지 쭉 내려감
      solution(g, node, visited)  
  
  return visited


graph = {
  1: [2, 3],
  2: [4, 5],
  3: [],
  4: [],
  5: []
}

# 좌로 DFS 잘한다. 정확함
print(solution(graph, 1))