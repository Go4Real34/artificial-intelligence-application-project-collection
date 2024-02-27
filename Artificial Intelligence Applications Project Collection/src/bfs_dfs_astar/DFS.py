from ..structures import Node, Stack

class DFS():
    def __init__(self, maze):
        self.maze = maze
        self.number_of_explored_nodes = 0
        self.explored_nodes = set()
        
        self.stack = Stack()
        start = Node(self.maze.start, None, None)
        self.stack.push(start)
        
        return
    