"""
Requirements:

pip install graphviz
"""

from graphviz import Digraph
from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root

            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        if self.root is None:
            return False
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            elif current_node.value == value:
                return current_node
        return False

    def traverse(self):
        """Breadth First Search"""
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result

def add_edges(graph, node):
    if node.left:
        graph.edge(str(node.value), str(node.left.value))
        add_edges(graph, node.left)
    if node.right:
        graph.edge(str(node.value), str(node.right.value))
        add_edges(graph, node.right)

def draw_bst(bst):
    dot = Digraph(comment='Binary Search Tree')

    if bst.root:
        dot.node(str(bst.root.value))
        add_edges(dot, bst.root)

        dot.render('bst', format='png', cleanup=True)
        dot.view('bst')

bst = BinarySearchTree()
values = [9, 4, 6, 20, 170, 15, 1]

for value in values:
    bst.insert(value)

draw_bst(bst)
