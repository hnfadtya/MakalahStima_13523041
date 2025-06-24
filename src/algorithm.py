import heapq
import math

def UCS(graph, start, goal):

    queue = [(0, [start], [])] # (time, path, moda)
    best_time = float('inf')
    best_path = []
    best_moda = []
    visited = {}
    visited_nodes_count = 0
    edges_explored = []

    while queue:
        total_time, path, moda_path = heapq.heappop(queue)
        current = path[-1]
        visited_nodes_count += 1

        if current in visited and total_time >= visited[current]:
            continue
        visited[current] = total_time

        if current == goal:
            if total_time < best_time:
                best_time = total_time
                best_path = path
                best_moda = moda_path
            continue

        for neighbor, time_cost, moda in graph[current]['edges']:
            if neighbor not in path:
                penalty = 5 if moda_path and moda_path[-1] != moda else 0
                heapq.heappush(queue, (total_time + time_cost + penalty, path + [neighbor], moda_path + [moda]))
                edges_explored.append((current, neighbor))

    return best_path, best_moda, best_time, visited_nodes_count, edges_explored

def euclidean_distance(node, goal, graph):
    x1, y1 = graph[node]['coords']
    x2, y2 = graph[goal]['coords']
    return math.dist((x1, y1), (x2, y2))

def astar(graph, start, goal):
    queue = [(0, 0, [start], [])]  # (f, g, path, moda_path)
    best_time = float('inf')
    best_path = []
    best_moda = []
    visited = {}
    visited_nodes_count = 0
    edges_explored = []

    while queue:
        f, g, path, moda_path = heapq.heappop(queue)
        current = path[-1]
        visited_nodes_count += 1

        if current in visited and g >= visited[current]:
            continue
        visited[current] = g

        if current == goal:
            if g < best_time:
                best_time = g
                best_path = path
                best_moda = moda_path
            continue

        for neighbor, time_cost, moda in graph[current]['edges']:
            if neighbor not in path:
                current_moda = moda_path[-1] if moda_path else None
                penalty = 5 if current_moda and current_moda != moda else 0

                new_g = g + time_cost + penalty
                h = euclidean_distance(neighbor, goal, graph) * 2.5
                f = new_g + h

                heapq.heappush(queue, (f, new_g, path + [neighbor], moda_path + [moda]))
                edges_explored.append((current, neighbor))

    return best_path, best_moda, best_time, visited_nodes_count, edges_explored