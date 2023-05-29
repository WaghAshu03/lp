from collections import deque


def get_graph(no_of_vertices):
    graph = {i+1: [] for i in range(no_of_vertices)}
    visited = []

    for i in range(no_of_vertices):
        for j in range(no_of_vertices):
            if (i == j):
                continue

            if (f"{i}|{j}" not in visited):
                print("-"*50)
                yesno = input(
                    f"Is there edge between {i + 1} & {j + 1}(y/n): ")

                if (yesno.lower() == 'y'):
                    graph[i + 1].append(j + 1)
                    graph[j + 1].append(i + 1)

                visited.append(f"{i}|{j}")
                visited.append(f"{j}|{i}")

    return graph


def bfs_recursive(graph, queue, visited, traversal_order):
    if not queue:
        return traversal_order

    vertex = queue.popleft()
    visited.add(vertex)
    traversal_order.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    return bfs_recursive(graph, queue, visited, traversal_order)


def bfs(graph, start):
    visited = set()
    traversal_order = []
    queue = deque([start])

    return bfs_recursive(graph, queue, visited, traversal_order)


def dfs(graph, start):
    visited = set()
    traversal_order = []

    def dfs_recursive(vertex):
        visited.add(vertex)
        traversal_order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return traversal_order


g = {
    1: [2, 4],
    2: [1, 3, 5, 7, 8],
    3: [2, 4, 9, 10],
    4: [1, 3],
    5: [2, 6, 7, 8],
    6: [5],
    7: [2, 5, 8],
    8: [2, 5, 7],
    9: [3],
    10: [3]
}


# vertices = int(input("Enter Number of vertices: "))
# g = get_graph(vertices)
print("="*50)
print("Graph:")
for key, value in g.items():
    print(f"{key}: {value}")
print("")
print("BFS:", bfs(g, 1))
print("DFS:", dfs(g, 1))
print("="*50)
