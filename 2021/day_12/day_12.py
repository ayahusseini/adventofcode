'''Solution to day 12 2021'''
from collections import defaultdict
from copy import deepcopy

INPUT_FILE = "inputs/day_12_input.txt"
TEST_FILE = "inputs/day_12_test_input.txt"

class PathError(ValueError):
    pass

class Path:
    """A path through the cave system"""
    def __init__(self, caves: list[str], start, end):
        self.caves = caves 
        self.start = start
        self.end = end
        self.visited_small_twice = False 
    
    def __str__(self) -> str:
        return str(self.caves)
    
    def is_complete(self) -> bool:
        return self.caves[0] == self.start and self.caves[-1] == self.end
    
    def _constraint(self, new_cave) -> bool:
        return not (new_cave.islower() and new_cave in self.caves)
    
    def add_cave_to_path(self,cave:str) -> list[str]:
        if self._constraint(cave):
            self.caves += [cave] 
            return 
        raise PathError("Constraint violated by adding the cave.")

class PathWithDoubleVisits(Path):
    """A path through the cave system that allows small caves to be visited twice""" 

    def __init__(self, caves, start, end):
        super().__init__(caves,start, end)

    def _constraint(self, new_cave:str):
        if self.visited_small_twice or new_cave in [self.start, self.end]:
            return super()._constraint(new_cave)
        elif new_cave in self.caves and new_cave.islower():
            self.visited_small_twice = True 
        return True 


class Map:
    """A map of the cave system"""
    def __init__(self,
                 cave_connections:list[tuple[str,str]],
                 start: str, 
                 end: str):
        '''Instantiates a map of caves'''
        
        self.start = start 
        self.end = end 
        
        self.connections = defaultdict(lambda: set())

        for connection in cave_connections:
            cave1, cave2 = connection
            self.connections[cave1].update([cave2])
            self.connections[cave2].update([cave1])

    @classmethod 
    def from_file_lines(cls, 
                        lines:list[str],
                        start_name:str, 
                        end_name:str):
        """Instantiate a map from a list of filelines"""
        connections = []
        for line in lines:
            line = line.replace("\n","").strip()
            
            connection = [cave for cave in line.split('-')]
            connections.append(tuple(connection))

        return cls(connections,start_name, end_name)
    
    def get_paths(self, path_type = Path):
        """Return all paths from start to end"""
        paths = []
        stack = [(self.start, path_type([self.start],self.start, self.end))]

        while stack: 

            cur_source, cur_path = stack.pop()

            for neighbour in self.connections[cur_source]:

                if neighbour == self.start:
                    continue
                elif neighbour == self.end:
                    new_path = deepcopy(cur_path)
                    new_path.add_cave_to_path(self.end)
                    paths.append(new_path)
                
                else:
                    try:
                        new_path = deepcopy(cur_path)
                        new_path.add_cave_to_path(neighbour)
                        stack.append((neighbour, new_path))
                    except PathError:
                        continue

        return paths 
    

def load_file(filename: str) -> list[str]:
    '''Loads the file as a list of strings'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return lines


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)
    map = Map.from_file_lines(lines,"start","end" )

    return len(map.get_paths(Path))


def two_star(filename: str):
    '''Returns the two star solution'''
    lines = load_file(filename)
    map = Map.from_file_lines(lines,"start","end")
    return len(map.get_paths(PathWithDoubleVisits))



if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
