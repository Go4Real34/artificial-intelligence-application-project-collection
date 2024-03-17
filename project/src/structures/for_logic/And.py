from .Sentence import Sentence

class And(Sentence):
    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence().validate(conjunct)
        self.conjuncts = list(conjuncts)
        return
    
    def __eq__(self, other):
        return (isinstance(other, And)) and (self.conjuncts == other.conjuncts)
    
    def __hash__(self):
        return hash(("and", tuple(hash(conjunct) for conjunct in self.conjuncts)))
    
    def __repr__(self):
        conjuctions = ", ".join([str(conjunct) for conjunct in self.conjuncts])
        return f"And({conjuctions})"
    
    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)
    
    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        
        return " ∧ ".join([Sentence().paranthesize(conjunct.formula()) for conjunct in self.conjuncts])
    
    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])
    
    def add(self, conjunct):
        Sentence().validate(conjunct)
        self.conjuncts.append(conjunct)
        return
    
    def modify(self, new_conjuncts):
        for new_conjunct in new_conjuncts:
            Sentence().validate(new_conjunct)
        self.conjuncts = list(new_conjuncts)
        return
    