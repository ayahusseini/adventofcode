'''Solution to day 12 2021'''

from collections import defaultdict


class CaveMap(object):
    '''Represents the nodes and paths on the map.'''

    def __init__(self):
        # maps nodes to the set of nodes they are directly connected to
        self.connections = defaultdict(lambda: set())
        self.visit_once_max = set()

    def add_edge(self, cave_1: str, cave_2: str):
        '''Updates the connections'''
        self.connections[cave_1].update([cave_2])
        self.connections[cave_2].update([cave_1])
        if cave_1.islower():
            self.visit_once_max.update([cave_1])
        if cave_2.islower():
            self.visit_once_max.update([cave_2])

    def find_cave_path(self, start: str, end: str):
        '''Find all cave paths from the start to the end'''
        paths = []

        curr_path = [start]
        visited = []
        # remove the first node to get the nearest neighbour to A
        neighbours = [start]

        while curr_path[-1] != end:
            next_cave = neighbours.pop()

            if next_cave not in visited


if __name__ == "__main__":
    ...
