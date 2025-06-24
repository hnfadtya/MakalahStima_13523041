import heapq
import time
import graph_route 

def branch_and_bound(graph, start, goal):
    start_time = time.time()  

    queue = [(0, [start], [])]
    best_time = float('inf')
    best_path = []
    best_moda = []
    visited = {}
    visited_nodes_count = 0

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

        for neighbor, time_cost, moda in graph.get(current, []):
            if neighbor not in path: # untuk menghindari siklus
                heapq.heappush(queue, (total_time + time_cost, path + [neighbor], moda_path + [moda]))

    elapsed_time = time.time() - start_time  
    return best_path, best_moda, best_time, visited_nodes_count, elapsed_time

def print_output(path, moda, total_time, start, goal, nodes, time):
    if path:
        print(f"\The fastest route from {start} to {goal}:")
        for i in range(len(path) - 1):
            print(f"{path[i]} ({moda[i]}) → ")
        print(f"{path[-1]}")
        print(f"Total duration to travel: {total_time} minute")
    else:
        print(f"Cannot find route from {start} to {goal}.")
    print(f"\nVisited Node: {nodes}")
    print(f"Elapsed Time: {time:5f} s")

def main():
    start = 'Tangerang'
    goal = 'Bekasi'

    path, moda, total_time, nodes, time = branch_and_bound(graph_route.graph_route, start, goal)
    print_output(path, moda, total_time, start, goal, nodes, time)

if __name__ == '__main__':
    main()