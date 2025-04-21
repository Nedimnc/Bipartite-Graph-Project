from collections import deque
from graph_data import graph  # If using graph_data.py

def is_bipartite(graph):
    color = {}
    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0  # Start with color 0
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        print(f"Conflict detected: Node {current} and Node {neighbor} have the same color.")
                        return False, color
    return True, color

# Run the checker
if __name__ == "__main__":
    result, coloring = is_bipartite(graph)
    print("\n✅ Is the graph bipartite (2-colorable)?", result)
    print("🎨 Node colors:", coloring)
