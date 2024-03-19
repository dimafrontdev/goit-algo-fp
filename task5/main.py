import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def bfs(root):
    queue, order = [root], []
    while queue:
        node = queue.pop(0)
        if node:
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order


def dfs(root):
    stack, order = [root], []
    while stack:
        node = stack.pop()
        if node:
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return order


def assign_colors(order):
    cmap = plt.get_cmap('Blues')
    n = len(order)
    for i, node in enumerate(order):
        color = mcolors.to_hex(cmap((i + 1) / (n + 1)))
        node.color = color


def draw_trees(root):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    # BFS
    bfs_order = bfs(root)
    assign_colors(bfs_order)
    tree_bfs = nx.DiGraph()
    pos_bfs = {root.id: (0, 0)}
    tree_bfs = add_edges(tree_bfs, root, pos_bfs)
    colors_bfs = [node[1]['color'] for node in tree_bfs.nodes(data=True)]
    labels_bfs = {node[0]: node[1]['label']
                  for node in tree_bfs.nodes(data=True)}
    nx.draw(tree_bfs, pos=pos_bfs, labels=labels_bfs, arrows=False,
            node_size=2500, node_color=colors_bfs, ax=axes[0])
    axes[0].set_title('Breadth-First Search')

    # DFS
    for node in bfs_order:
        node.color = "skyblue"
    dfs_order = dfs(root)

    assign_colors(dfs_order)
    tree_dfs = nx.DiGraph()
    pos_dfs = {root.id: (0, 0)}
    tree_dfs = add_edges(tree_dfs, root, pos_dfs)
    colors_dfs = [node[1]['color'] for node in tree_dfs.nodes(data=True)]
    labels_dfs = {node[0]: node[1]['label']
                  for node in tree_dfs.nodes(data=True)}
    nx.draw(tree_dfs, pos=pos_dfs, labels=labels_dfs, arrows=False,
            node_size=2500, node_color=colors_dfs, ax=axes[1])
    axes[1].set_title('Depth-First Search')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.left.left = Node(8)
    root.left.right = Node(10)
    root.left.right.left = Node(11)
    root.left.right.right = Node(12)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right = Node(2)
    root.right.right.left = Node(9)

    draw_trees(root)
