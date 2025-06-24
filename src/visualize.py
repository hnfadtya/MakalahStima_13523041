import networkx as nx
import matplotlib.pyplot as plt

def visualize_tree(edges, solution_path=None, save_as=None):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, seed=42, k=0.5)

    # Tentukan warna node
    node_colors = []
    for node in G.nodes():
        if solution_path and node in solution_path:
            node_colors.append("limegreen")  # hijau: jalur solusi
        else:
            node_colors.append("skyblue")    # biru: simpul lainnya

    edge_colors = []
    for edge in G.edges():
        if solution_path and edge in zip(solution_path, solution_path[1:]):
            edge_colors.append("green")
        else:
            edge_colors.append("gray")

    plt.figure(figsize=(14, 10))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=2500,
        font_size=9,
        font_weight='bold',
        arrows=True,
        arrowstyle='->',
        arrowsize=20,
    )

    plt.title("State Space Tree for Route Search", fontsize=16, fontweight='bold')
    plt.margins(0.2)    
    plt.show()
    if save_as:
        plt.savefig(save_as, dpi=300)
        print(f"Saved graph to {save_as}")
    else:
        plt.show()
