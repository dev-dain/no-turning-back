# DFS (정석) 스택 이용
# dfs에는 스택을 쓴다
# visited가 꼭 있어야 함. 
def solution(g, start):
  st = [start] # 아예 넣으면서 시작 가능
  visited = []  # 방문했는지 아닌지 보기

  while st:
    el = st.pop() # pop을 쓴다 popleft() 대신
    print(el)
    if el not in visited:
      visited.append(el)
      st += g.get(el)
  
  return visited


graph = {
  1: [2, 3],
  2: [4, 5],
  3: [],
  4: [],
  5: []
}

print(solution(graph, 1))