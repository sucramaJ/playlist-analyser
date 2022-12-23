class Node:
    def __init__(self, value, neighbours=None) -> None:
        self.value = value
        if neighbours is None:
            self.neighbours = []
        else:
            self.neighbours = neighbours
    def has_neighbours(self):
        if len(self.neighbours):
            return True
        return False
    def number_of_neighbours(self):
        return len(self.neighbours)

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

class Graph:
    def __init__(self, nodes=None) -> None:
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)


if __name__ == '__main__':
    node = Node(0)
    print(hash(node))
        