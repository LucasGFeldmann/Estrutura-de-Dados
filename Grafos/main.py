"""
Crie um grafo conexo com 10 cidades e as distâncias entre elas e depois realize as análises dos circuitos Euleriano e Hamiltoniano.

Utilize o módulo networkx para usar a estrutura de grafos

plote o grafo em forma gráfica.
desafio: indique o grafo e os trajetos calculados em cores diferentes.
"""

import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo conexo com 10 cidades
G = nx.Graph()

# Adicionar 10 nós
G.add_nodes_from(range(1,11))

# Adicionar arestas com pesos (distâncias)
edges = [
    (1, 2, 10),
    (1, 5, 10),
    (1, 7, 15),
    (1, 6, 5),
    (2, 3, 5),
    (2, 4, 10),
    (2, 9, 15),
    (2, 10, 5),
    (2, 8, 5),
    (3, 4, 5),
    (3, 10, 15),
    (4, 5, 10),
    (6, 7, 10),
    (6, 5, 5),
    (7, 8, 5),
    (8, 9, 10),
    (9, 10, 10)
]

# Adicionar arestas ao grafo
G.add_weighted_edges_from(edges)

# Verificar conectividade
assert nx.is_connected(G), "O grafo não está conectado."

# Plotar o grafo
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()

# Verificação de circuito Euleriano
eulerian_circuit = None
if nx.is_eulerian(G):
    eulerian_circuit = list(nx.eulerian_circuit(G))
    print("O grafo possui um circuito Euleriano:", eulerian_circuit)
else:
    print("O grafo não possui um circuito Euleriano.")

# Verificação de circuito Hamiltoniano
def hamiltonian_path(G, start):
    path = [start]
    visited = set(path)
    n = len(G)

    def backtrack(v):
        if len(path) == n:
            return path
        for u in G[v]:
            if u not in visited:
                path.append(u)
                visited.add(u)
                result = backtrack(u)
                if result:
                    return result
                visited.remove(u)
                path.pop()
        return None

    return backtrack(start)

hamiltonian_circuit = None
for node in G.nodes:
    path = hamiltonian_path(G, node)
    if path:
        hamiltonian_circuit = path + [path[0]]
        break

if hamiltonian_circuit:
    print("O grafo possui um circuito Hamiltoniano:", hamiltonian_circuit)
else:
    print("O grafo não possui um circuito Hamiltoniano.")

# Plotar os circuitos se existirem
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# Plotar circuito Euleriano em vermelho
if eulerian_circuit:
    eulerian_edges = [(u, v) for u, v in eulerian_circuit]
    nx.draw_networkx_edges(G, pos, edgelist=eulerian_edges, edge_color='red', width=2)

# Plotar o circuito Hamiltoniano se existir
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Plotar circuito Hamiltoniano em verde
if hamiltonian_circuit:
    hamiltonian_edges = [(hamiltonian_circuit[i], hamiltonian_circuit[i+1]) for i in range(len(hamiltonian_circuit)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=hamiltonian_edges, edge_color='green', width=2)

plt.show()

# Calcular e plotar o caminho ótimo do nó 3 para o nó 10 usando o algoritmo de Dijkstra
source, target = 6, 10
shortest_path = nx.dijkstra_path(G, source=source, target=target)
print(f"O caminho ótimo do nó {source} para o nó {target} é:", shortest_path)

# Plotar o grafo e o caminho ótimo
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=14, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# Plotar o caminho ótimo em azul
optimal_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
nx.draw_networkx_edges(G, pos, edgelist=optimal_path_edges, edge_color='blue', width=2)

plt.show()