import heapq

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
        # print(f"Current atau path[-1]: {current}")
        visited_nodes_count += 1

        if current in visited and total_time >= visited[current]:
            # print(f"current in visited and total_time >= visited[current]: {total_time} >= {visited[current]}")
            continue
        visited[current] = total_time
        # print(visited)

        if current == goal:
            if total_time < best_time:
                best_time = total_time
                best_path = path
                best_moda = moda_path
            continue

        for neighbor, time_cost, moda in graph.get(current, []):
            if (neighbor not in path): # untuk menghindari siklus
                heapq.heappush(queue, (total_time + time_cost, path + [neighbor], moda_path + [moda]))
                edges_explored.append((current, neighbor))

        # for path in queue:
        #     print(path)

    return best_path, best_moda, best_time, visited_nodes_count, edges_explored

def heuristic(node, goal, current_moda):
    transit_penalty = 5 if current_moda else 0 # Penalti jika harus ganti moda
    return transit_penalty

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
        print(f"Current atau path[-1]: {current}")
        visited_nodes_count += 1

        if current in visited and g >= visited[current]:
            print(f"current in visited and total_time >= visited[current]: {g} >= {visited[current]}")
            continue
        visited[current] = g

        if current == goal:
            if g < best_time:
                best_time = g
                best_path = path
                best_moda = moda_path
            continue

        for neighbor, time_cost, moda in graph.get(current, []):
            if neighbor not in path:
                new_g = g + time_cost
                current_moda = moda_path[-1] if moda_path else None
                h = heuristic(neighbor, goal, moda if current_moda != moda else None)
                f = new_g + h
                heapq.heappush(queue, (f, new_g, path + [neighbor], moda_path + [moda]))
                edges_explored.append((current, neighbor))

        for path in queue:
            print(path)

    return best_path, best_moda, best_time, visited_nodes_count, edges_explored