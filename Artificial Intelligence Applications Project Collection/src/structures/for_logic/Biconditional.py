from .Sentence import Sentence

class Biconditional(Sentence):
    def __init__(self, left, right):
        Sentence.validate(left)
        self.left = left
        
        Sentence.validate(right)
        self.right = right
        
        return
    
    def __eq__(self, other):
        return (isinstance(other, Biconditional) and ((self.left == other.left) and (self.right == other.right)))
    
    def __hash__(self):
        return (("iff", hash(self.left), hash(self.right)))
    
    def __repr__(self):
        return f"Biconditional({self.left}, {self.right})"
    