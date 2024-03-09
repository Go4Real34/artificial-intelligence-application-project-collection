from .Sentence import Sentence

class Implication(Sentence):
    def __init__(self, antecedent, consequent):
        Sentence.validate(antecedent)
        self.antecedent = antecedent
        
        Sentence.validate(consequent)
        self.consequent = consequent
        
        return
    
    def __eq__(self, other):
        return (isinstance(other, Implication)) and ((self.antecedent == other.antecedent) and (self.consequent == other.consequent))
    
    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))
    
    def __repr__(self):
        return f"Implication({self.antecedent}, {self.consequent})"
    