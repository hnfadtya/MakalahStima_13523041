import algorithm
import graph_route 
import time
from visualize import visualize_tree

def print_output(path, moda, total_time, start, goal, nodes, elapsed_time):
    if path:
        print(f"\nThe fastest route from {start} to {goal}:")
        for i in range(len(path) - 1):
            print(f"{path[i]} ({moda[i]}) → ")
        print(path[-1])
        print(f"Total travel time: {total_time} minutes")
    else:
        print(f"No route found from {start} to {goal}.")
    print(f"Nodes visited: {nodes}")
    print(f"Time taken: {elapsed_time:.5f} µs\n")

def main():
    while True:
        graph = graph_route.graph_route
        print("=== Public Transport Route Finder ===")

        action = input("Enter 'Quit' to exit or anything else to continue...\n").strip()
        if action == "Quit":
            print("Exiting...")
            break

        start = input("Enter START location: ").strip()
        goal = input("Enter GOAL location: ").strip()

        while start not in graph or goal not in graph:
            print("Invalid start or goal location.")
            start = input("Enter START location: ").strip()
            goal = input("Enter GOAL location: ").strip()

        print("\nChoose search algorithm:")
        print("1. Uniform Cost Search (UCS)")
        print("2. A* Search")
        algo = input("Enter 1 or 2: ").strip()

        start_time = time.time()

        if algo == '1':
            path, moda, total_time, nodes, edges_explored = algorithm.UCS(graph, start, goal)
        elif algo == '2':
            path, moda, total_time, nodes, edges_explored = algorithm.astar(graph, start, goal)
        else:
            print("Invalid algorithm choice.")
            return

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1_000_000
        print_output(path, moda, total_time, start, goal, nodes, elapsed_time)

        print("Visualizing state space tree...")
        visualize_tree(edges_explored, path, "state_tree.png")

if __name__ == '__main__':
    main()