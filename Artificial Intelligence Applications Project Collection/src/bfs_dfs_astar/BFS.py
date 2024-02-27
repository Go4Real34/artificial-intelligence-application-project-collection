from ..structures import Node, Queue

class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.number_of_explored_nodes = 0
        self.explored_nodes = set()
        
        self.frontier = Queue()
        start = Node(self.maze.start, None, None)
        self.frontier.push(start)
        
        return
    