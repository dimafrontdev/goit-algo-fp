import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            self._heapify_up(parent_index)


class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap_array):
    nodes = [HeapNode(val) for val in heap_array]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Вибір кольору вузла в залежності від його рівня у дереві
        color_scale = list(mcolors.TABLEAU_COLORS)  # Список доступних кольорів
        node.color = color_scale[
            layer % len(color_scale)
        ]  # Перебір кольорів для різних рівнів

        graph.add_node(node.id, color=node.color, label=node.val)
        if hasattr(node, "left") and node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if hasattr(node, "right") and node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_root):
    tree = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    tree = add_edges(tree, heap_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        node_size=2500,
        node_color=colors,
        with_labels=True,
        arrows=False,
    )
    plt.show()


if __name__ == "__main__":
    # Приклад створення і відображення бінарної купи
    heap = MinHeap()
    data = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    for item in data:
        heap.insert(item)

    heap_root = build_heap_tree(heap.heap)
    draw_heap(heap_root)
