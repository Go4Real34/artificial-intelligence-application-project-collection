from .Sentence import Sentence

class Symbol(Sentence):
    def __init__(self, name):
        self.name = name
        return
    
    def __eq__(self, other):
        return (isinstance(other, Symbol)) and (self.name == other.name)
    
    def __hash__(self):
        return hash(("symbol", self.name))
    
    def __repr__(self):
        return self.name
    