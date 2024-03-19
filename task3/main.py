import networkx as nx
import heapq
import matplotlib.pyplot as plt


def dijkstra_algorithm(graph, start):
    # Ініціалізація відстаней та попередників
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    predecessors = {vertex: None for vertex in graph.nodes}
    distances[start] = 0
    # Ініціалізація купи
    queue = [(0, start)]

    while queue:
        # Вибірка вершини з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(queue)

        # Огляд сусідніх вершин
        for neighbor, details in graph[current_vertex].items():
            distance = details["weight"]
            new_distance = current_distance + distance

            # Оновлення відстані, якщо знайдено коротший шлях
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(queue, (new_distance, neighbor))

    return distances, predecessors


def plot_graph_with_paths(G, distances, start):
    pos = nx.spring_layout(G)  # Розташування вершин за допомогою spring layout

    # Візуалізація графа
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=700,
        edge_color="k",
        linewidths=1,
        font_size=15,
        font_weight="bold",
    )

    # Підпис ваг ребер
    edge_labels = dict(
        [
            (
                (
                    u,
                    v,
                ),
                d["weight"],
            )
            for u, v, d in G.edges(data=True)
        ]
    )
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=12
    )

    # Виділення шляхів від початкової вершини до всіх інших
    for end in distances:
        if end != start:
            path = nx.shortest_path(
                G, source=start, target=end, weight="weight")
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=[(path[i], path[i + 1])
                          for i in range(len(path) - 1)],
                width=2,
                edge_color="r",
            )
            nx.draw_networkx_nodes(
                G, pos, nodelist=path, node_color="lightgreen", node_size=700
            )

    plt.title(f"Найкоротші шляхи від вершини {start}")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    # Створення зваженого графа
    G = nx.Graph()
    G.add_weighted_edges_from(
        [
            (1, 2, 1),
            (1, 3, 4),
            (2, 3, 2),
            (2, 4, 5),
            (3, 5, 3),
            (4, 5, 1),
            (4, 6, 2),
            (5, 6, 4),
        ]
    )

    distances, predecessors = dijkstra_algorithm(G, 1)

    for vertex, distance in distances.items():
        print(f"Відстань від вершини 1 до вершини {vertex}: {distance}")

    # Візуалізація графа з найкоротшими шляхами від вершини 1
    plot_graph_with_paths(G, distances, 1)
