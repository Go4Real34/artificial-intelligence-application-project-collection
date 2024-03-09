from .Sentence import Sentence

class Implication(Sentence):
    def __init__(self, antecedent, consequent):
        Sentence().validate(antecedent)
        self.antecedent = antecedent
        
        Sentence().validate(consequent)
        self.consequent = consequent
        
        return
    
    def __eq__(self, other):
        return (isinstance(other, Implication)) and ((self.antecedent == other.antecedent) and (self.consequent == other.consequent))
    
    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))
    
    def __repr__(self):
        return f"Implication({self.antecedent}, {self.consequent})"
    
    def evaluate(self, model):
        return ((not self.antecedent.evaluate(model)) or (self.consequent.evaluate(model)))
    
    def formula(self):
        antecedent = Sentence().paranthesize(self.antecedent.formula())
        consequent = Sentence().paranthesize(self.consequent.formula())
        return f"{antecedent} -> {consequent}"
    
    def symbols(self):
        return set.union(self.antecedent.symbols(), self.consequent.symbols())
    
    def modify(self, new_antecedent, new_consequent):
        Sentence().validate(new_antecedent)
        self.antecedent = new_antecedent
        
        Sentence().validate(new_consequent)
        self.consequent = new_consequent
        return
    