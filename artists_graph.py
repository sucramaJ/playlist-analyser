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
        