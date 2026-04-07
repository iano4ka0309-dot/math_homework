import networkx as nx
import matplotlib.pyplot as plt

graf = {
    'Анна': ['Богдан', 'Віктор', 'Ганна'],
    'Богдан': ['Анна', 'Віктор', 'Дмитро'],
    'Віктор': ['Анна', 'Богдан', 'Ганна', 'Дмитро'],
    'Ганна': ['Анна', 'Віктор', 'Євген'],
    'Дмитро': ['Богдан', 'Віктор', 'Євген'],
    'Євген': ['Ганна', 'Дмитро']
}

G = nx.Graph(graf)

matrix = nx.to_numpy_array(G, nodelist=list(graf.keys()), dtype=int)
print("Матриця суміжності:")
print(f"{'':10}", end="")
for name in graf.keys():
    print(f"{name:8}", end="")
print()

for i, name in enumerate(graf.keys()):
    print(f"{name:10}", end="")
    for val in matrix[i]:
        print(f"{val:<8}", end="")
    print()

print("\nРебра графа:")
for edge in G.edges():
    print(edge)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, 
        with_labels=True, 
        node_color='lightblue', 
        node_size=1500, 
        font_size=10, 
        font_weight='bold')

plt.title("Граф зв'язків")
plt.show()


print("\nСтепені вершин:")
for person in graf:
    degree = len(graf[person])
    print(f"{person}: {degree}")

total_degree = sum(len(graf[p]) for p in graf)


max_person = max(graf, key=lambda p: len(graf[p]))
min_person = min(graf, key=lambda p: len(graf[p]))
print(f"Найбільш комунікабельний: {max_person}")
print(f"Найменш комунікабельний: {min_person}")


edges_count = len(list(G.edges()))
print(f"\nКількість ребер: {edges_count}")
print(f"Сума степенів: {total_degree}")
print(f"2 × ребра = {2 * edges_count}")
print(f"Теорема виконується: {total_degree == 2 * edges_count}")

