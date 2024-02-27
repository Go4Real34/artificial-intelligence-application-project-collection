class Queue:
    def __init__(self):
        self.frontier = []
        
        return
    
    def push(self, node):
        self.frontier.append(node)
        
        return
    
    def is_empty(self):
        return len(self.frontier) == 0
    
    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop Node object: Queue frontier is empty!")
        
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
    