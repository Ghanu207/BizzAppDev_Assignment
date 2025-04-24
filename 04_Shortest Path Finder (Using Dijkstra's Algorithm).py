"""
1. Use a priority queue to explore nodes in order of increasing distance.
2. Maintain a dictionary for shortest distances and parent tracking.
3. Reconstruct the path once destination is reached.
"""

import heapq

def dijkstra(graph, start, destination):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        (cost, current_city, path) = heapq.heappop(heap)
        if current_city in visited:
            continue
        visited.add(current_city)
        path = path + [current_city]

        if current_city == destination:
            return (path, cost)

        for neighbor, weight in graph[current_city].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path))

    return ([], float('inf'))

# Example input
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'

path, distance = dijkstra(graph, start_city, destination_city)
print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(path)}")
print(f"Total distance: {distance}")
