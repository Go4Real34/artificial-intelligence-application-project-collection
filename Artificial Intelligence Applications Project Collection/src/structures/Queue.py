class Queue:
    def __init__(self):
        self.frontier = []
        
        return
    
    def push(self, node):
        self.frontier.append(node)
        
        return
    
    def is_empty(self):
        return len(self.frontier) == 0
    