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
    
    def g_n(self, cost):
        return cost + 1
    
    def h_n(self, state):
        goal_row, goal_column = self.maze.goal
        row, column = state
        return abs(goal_row - row) + abs(goal_column - column)
    
    def gn_plus_hn(self, node_with_cost):
        node, cost = node_with_cost
        return (self.g_n(cost) + self.h_n(node.state))
    