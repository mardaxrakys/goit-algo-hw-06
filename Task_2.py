# Пошук в глибину (DFS)
dfs_path = list(nx.dfs_edges(G, source='A'))
print("DFS шлях: ", dfs_path)

# Пошук в ширину (BFS)
bfs_path = list(nx.bfs_edges(G, source='A'))
print("BFS шлях: ", bfs_path)
