from ..structures import Node, Queue

class ASTAR:
    def __init__(self, maze):
        self.maze = maze
        self.number_of_explored_nodes = 0
        self.explored_nodes = set()
        
        self.queue = Queue()
        start = (Node(self.maze.start, None, None), 0)
        self.queue.push(start)
        
        return
    