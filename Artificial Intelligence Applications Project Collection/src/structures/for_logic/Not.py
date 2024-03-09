from .Sentence import Sentence

class Not(Sentence):
    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand
        return
    
    def __eq__(self, other):
        return (isinstance(other, Not)) and (self.operand == other.operand)
    
    def __hash__(self):
        return hash(("not", hash(self.operand)))
    
    def __repr__(self):
        return f"Not({self.operand})"
    