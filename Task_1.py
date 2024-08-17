import networkx as nx
import matplotlib.pyplot as plt

# Створення неорієнтованого графа
G = nx.Graph()

# Додавання вершин
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Додавання ребер
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')])

# Візуалізація графа
pos = nx.spring_layout(G)  # визначення позицій вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=16, font_weight='bold')
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = [degree for node, degree in G.degree()]

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degrees}")
