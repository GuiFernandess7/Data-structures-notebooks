import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    G = nx.Graph()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            G.add_node(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    G.add_node(neighbor)
                    G.add_edge(node, neighbor)
                    queue.append(neighbor)

    return G

""" graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D', 'F'],
    'D': ['H', 'G', 'I', 'C'],
    'E': [],
    'F': ['J', 'C', 'G'],
    'G': ['F', 'D'],
    'H': ['D'],
    'I': ['J', 'D'],
    'J': ['F', 'I'],
} """

""" graph = {
    '0': ['1', '2'],
    '1': ['0', '4', '3', '2'],
    '2': ['0', '1'],
    '3': ['5', '1'],
    '4': ['1'],
    '5': ['8', '6', '7', '3'],
    '6': ['5'],
    '7': ['5', '8'],
    '8': ['5', '9'],
    '9': ['8']

} """

""" graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'B': 5, 'D': 3, 'C': 2},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 5},
    'D': {'B': 3, 'C': 4, 'E': 2, 'F': 2},
    'E': {'F': 4, 'D': 2, 'C': 5},
    'F': {'D': 2, 'E': 4},
} """


graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
    'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
    'E': {'F': 5, 'D': 11, 'C': 1},
    'F': {'D': 22, 'E': 1},
}

start_node = 'A'
bfs_graph = bfs(graph, start_node)

pos = nx.spring_layout(bfs_graph)
nx.draw(bfs_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
plt.show()
