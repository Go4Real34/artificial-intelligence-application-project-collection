from .Sentence import Sentence

class Biconditional(Sentence):
    def __init__(self, left, right):
        Sentence().validate(left)
        self.left = left
        
        Sentence().validate(right)
        self.right = right
        
        return
    
    def __eq__(self, other):
        return (isinstance(other, Biconditional) and ((self.left == other.left) and (self.right == other.right)))
    
    def __hash__(self):
        return (("iff", hash(self.left), hash(self.right)))
    
    def __repr__(self):
        return f"Biconditional({self.left}, {self.right})"
    
    def evaluate(self, model):
        return (((self.left.evaluate(model)) and (self.right.evaluate(model))) or ((not (self.left.evaluate(model))) and (not (self.left.evaluate(model)))))
    
    def formula(self):
        left = Sentence().paranthesize(str(self.left))
        right = Sentence().paranthesize(str(self.right))
        return f"{left} <-> {right}"

    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())
    
    def modify(self, new_left, new_right):
        Sentence().validate(new_left)
        self.left = new_left
        
        Sentence().validate(new_right)
        self.right = new_right
        return
    