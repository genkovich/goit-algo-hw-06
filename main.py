import networkx as nx
import matplotlib.pyplot as plt
from graph_generator import generate_fb_friends
from algorithm import dijkstra, dfs, bfs


def main():
    main_account_name = "My Facebook Account"

    fb_friends, friend_for_search = generate_fb_friends(main_account_name)
    # Draw the simplified random graph with names
    plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(fb_friends)
    nx.draw(fb_friends, pos, node_size=50, with_labels=True, node_color='skyblue', edge_color='gray', font_size=12)
    plt.title("Simplified Random Facebook Friends Network with Names")

    print(f"Friends count: {fb_friends.number_of_nodes()}")
    print(f"Connections count: {fb_friends.number_of_edges()}")
    print(f"Degree centrality: {nx.degree_centrality(fb_friends)}")
    plt.show()

    # Shortest path
    print(f"Shortest path between {main_account_name} and '{friend_for_search}':")
    shortest_path = nx.shortest_path(fb_friends, source=main_account_name, target=friend_for_search)
    print(shortest_path)

    # Dijkstra
    dijkstra_result = nx.single_source_dijkstra_path_length(fb_friends, main_account_name, cutoff=None, weight='weight')
    print(f"Dijkstra {main_account_name} and '{friend_for_search}': {dijkstra_result[friend_for_search]}")

    # Manual Dijkstra
    dijkstra_manual_result = dijkstra(fb_friends, main_account_name)
    print(f"Manual Dijkstra {main_account_name} and '{friend_for_search}': {dijkstra_manual_result[friend_for_search]}")

    # DFS
    dfs_tree = nx.dfs_tree(fb_friends, source=main_account_name)
    print("\nDFS")
    print(list(dfs_tree.edges()))
    print(list(dfs_tree.nodes()))
    # BFS
    bfs_tree = nx.bfs_tree(fb_friends, source=main_account_name)
    print("\nBFS")
    print(list(bfs_tree.edges()))
    print(list(bfs_tree.nodes()))

    # dfs manual
    dfs_manual = dfs(fb_friends, main_account_name)
    print("\nDFS manual")
    print(dfs_manual)

    # bfs manual
    bfs_manual = bfs(fb_friends, main_account_name)
    print("\nBFS manual")
    print(bfs_manual)


if __name__ == '__main__':
    main()

