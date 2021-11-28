import random


class Node:
    def __init__(self, p):
        self.left = None
        self.right = None
        self.parent = None
        self.value = p
        self.height = 0


class Heap:
    def __init__(self):
        self.nodes = []
        self.root = None
        pass

    def insert(self, p, node):
        if self.root is None:
            self.root = Node(p)
            return
        if node is None:
            node = self.root

        if node.left is None:
            node.left = Node(p)
            node.left.parent = node
            return self._correctTop(node.left)

        if node.right is None:
            node.right = Node(p)
            node.right.parent = node
            return self._correctTop(node.right)

        rand = random.uniform(0, 1)
        if rand == 0:
            self.insert(p, node.left)
        else:
            self.insert(p, node.right)

    def extractMax(self):
        pass

    def _correctTop(self, node):
        if node.parent.value >= node.value:
            return

        if node.parent.left == node:
            node.parent.left = None

        if node.parent.right == node:
            node.parent.right = None

        if node.left:
            pass
        if node.right:
            pass

        node.parent, node.parent.parent = node.parent.parent, node.parent

        pass


def main():
    pass


if __name__ == "__main__":
    main()
