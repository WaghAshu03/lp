import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices in the graph
        # Adjacency matrix representing the graph
        self.graph = [[0] * self.V for _ in range(self.V)]

    def add_edge(self, u, v, weight):
        # Add an edge to the graph by updating the adjacency matrix with the corresponding weight
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_distance(self, dist, visited):
        # Find the vertex with the minimum distance among the unvisited vertices
        min_dist = sys.maxsize  # Initialize the minimum distance to a large value
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        # Initialize the distances to all vertices as infinity
        dist = [sys.maxsize] * self.V
        dist[src] = 0  # Distance to the source vertex is set to 0
        # Initialize the visited array to track visited vertices
        visited = [False] * self.V

        for _ in range(self.V):
            # Find the vertex with the minimum distance
            u = self.min_distance(dist, visited)

            # Mark the vertex as visited
            visited[u] = True

            # Update the distances of neighboring vertices if a shorter path is found
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not visited[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist


# Example usage:
g = Graph(6)  # Create a graph with 6 vertices
g.add_edge(0, 1, 2)  # Add an edge between vertex 0 and vertex 1 with weight 2
g.add_edge(0, 2, 4)  # Add an edge between vertex 0 and vertex 2 with weight 4
g.add_edge(1, 2, 1)  # Add an edge between vertex 1 and vertex 2 with weight 1
g.add_edge(1, 3, 7)  # Add an edge between vertex 1 and vertex 3 with weight 7
g.add_edge(2, 4, 3)  # Add an edge between vertex 2 and vertex 4 with weight 3
g.add_edge(3, 4, 2)  # Add an edge between vertex 3 and vertex 4 with weight 2
g.add_edge(3, 5, 1)  # Add an edge between vertex 3 and vertex 5 with weight 1
g.add_edge(4, 5, 5)  # Add an edge between vertex 4 and vertex 5 with weight 5

source = 0  # Source vertex for Dijkstra's algorithm
# Calculate the shortest distances from the source vertex
shortest_distances = g.dijkstra(source)
print(f"Shortest distances from source vertex {source}:")
for v in range(g.V):
    # Print the shortest distance for each vertex
    print(f"Vertex {v}: {shortest_distances[v]}")
