
from collections import deque
import heapq

# Weighted Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Breadth First Search
def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    cost = 0

    while queue:
        node, path, distance = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        cost += 1

        if node == goal:
            return path, distance, cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                queue.append(
                    (neighbor, path + [neighbor],
                     distance + weight)
                )

    return None, float('inf'), cost


# Depth First Search
def dfs(graph, start, goal):
    stack = [(start, [start], 0)]
    visited = set()
    cost = 0

    while stack:
        node, path, distance = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        cost += 1

        if node == goal:
            return path, distance, cost

        for neighbor, weight in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [neighbor],
                     distance + weight)
                )

    return None, float('inf'), cost


# Uniform Cost Search
def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()
    cost = 0

    while priority_queue:
        distance, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        cost += 1

        if node == goal:
            return path, distance, cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (distance + weight,
                     neighbor, path + [neighbor])
                )

    return None, float('inf'), cost


# Main Program
start = 'A'
goal = 'G'

algorithms = [
    ("BFS", bfs),
    ("DFS", dfs),
    ("UCS", ucs)
]

print("SEARCH ALGORITHM COMPARISON")
print("-" * 55)

for name, algorithm in algorithms:
    path, distance, nodes = algorithm(graph, start, goal)

    print("\nAlgorithm:", name)
    print("Path:", " -> ".join(path) if path else "Not Found")
    print("Path Cost:", distance)
    print("Nodes Expanded:", nodes)
