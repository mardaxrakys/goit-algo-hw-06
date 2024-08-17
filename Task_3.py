# Створення графа з вагами
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from([('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 5), ('B', 'D', 10), ('C', 'D', 3), ('D', 'E', 1)])

# Найкоротший шлях від 'A' до всіх інших вершин
shortest_paths = nx.single_source_dijkstra_path_length(G_weighted, source='A')
print("Найкоротші відстані від 'A':", shortest_paths)

# Найкоротший шлях від 'A' до 'E'
path_A_to_E = nx.shortest_path(G_weighted, source='A', target='E', weight='weight')
print("Найкоротший шлях від 'A' до 'E':", path_A_to_E)
