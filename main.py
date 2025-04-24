from collections import deque  # Import deque for efficient queue operations (used in BFS)
from graph_data import graph  # Import the graph (as an adjacency list)

# Function to check if a graph is bipartite using 2-coloring and BFS
def is_bipartite(graph):
    color = {}  # Dictionary to store the color of each node (0 or 1)
    
    for node in graph:
        if node not in color:
            queue = deque([node])  # Start BFS with the current node
            color[node] = 0        # Assign initial color (0)

            while queue:
                current = queue.popleft()  # Get the next node from the queue

                for neighbor in graph[current]:  # Check all connected neighbors
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]  # Assign opposite color
                        queue.append(neighbor)  # Add neighbor to queue for further exploration
                    elif color[neighbor] == color[current]:
                        # If a neighbor has the same color → graph is not bipartite
                        print(f"Conflict detected: Node {current} and Node {neighbor} have the same color.")
                        return False, color

    # If we get through the whole graph with no conflicts, it's bipartite
    return True, color

# Run the bipartite checker and display results
if __name__ == "__main__":
    result, coloring = is_bipartite(graph)
    print("\n✅ Is the graph bipartite (2-colorable)?", result)
    print("🎨 Node colors:", coloring)
