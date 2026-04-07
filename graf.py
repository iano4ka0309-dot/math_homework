import networkx as nx
import matplotlib.pyplot as plt

graf = {'Анна': ['Богдан', 'Віктор', 'Ганна'],
         'Богдан': ['Анна', 'Віктор', 'Дмитро'],
         'Віктор': ['Анна', 'Богдан', 'Ганна', 'Дмитро'],
         'Ганна': ['Анна', 'Віктор', 'Євген'],
         'Дмитро': ['Богдан', 'Віктор', 'Євген'],
         'Євген': ['Ганна', 'Дмитро']}

people = list(graf.keys())
matrix = []
for person in people:
    row = []
    for other_person in people:
        if other_person in graf[person]:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print("Матриця суміжності:")
print(f"{'':10}", end="")
for name in people:
    print(f"{name:8}", end="")
print()

for i, row in enumerate(matrix):
    print(f"{people[i]:10}", end="")
    for val in row:
        print(f"{val:<8}", end="")
    print()
G = nx.Graph()

# Додаємо вузли (людей)
G.add_nodes_from(graf.keys())
# Додаємо ребра (зв'язки)
edges = []
for person in graf:
    for other in graf[person]:
        if person < other:
            edges.append((person, other))
G.add_edges_from(edges)
print("\nРебра графа:")
for edge in edges:
    print(edge)

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold')
plt.title("Граф зв'язків")
plt.show()
