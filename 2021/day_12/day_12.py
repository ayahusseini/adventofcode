'''Solution to day 12 2021'''
from collections import defaultdict
INPUT_FILE = "inputs/day_12_input.txt"
TEST_FILE = "inputs/day_12_test_input.txt"

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
    
    def get_paths(self):
        """Return all paths from start to end"""
        paths = []
        stack = [(self.start,[self.start])]

        while stack: 

            cur_source, cur_path = stack.pop()

            if cur_source == self.end:
                paths += [cur_path]

            else:
                for neighbour in self.connections[cur_source]:
                    if not (neighbour.islower() and neighbour in cur_path):
                        stack += [(neighbour, cur_path + [neighbour])]

        return paths 
    

def load_file(filename: str) -> list[str]:
    '''Loads the file as a list of strings'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return lines


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)
    map = Map.from_file_lines(lines,"start","end")

    return len(map.get_paths())


def two_star(filename: str):
    '''Returns the two star solution'''
    lines = load_file(filename)
    return 



if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    #print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
