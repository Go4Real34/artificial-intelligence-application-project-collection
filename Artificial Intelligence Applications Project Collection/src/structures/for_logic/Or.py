from .Sentence import Sentence

class Or(Sentence):
    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence().validate(disjunct)
            
        self.disjuncts = list(disjuncts)
        return
    
    def __eq__(self, other):
        return (isinstance(other, Or)) and (self.disjuncts == other.disjuncts)
    
    def __hash__(self):
        return hash(("or", tuple(hash(disjunct) for disjunct in self.disjuncts)))
    
    def __repr__(self):
        disjunts = ", ".join([str(disjunct) for disjunct in self.disjuncts])
        return f"Or({disjunts})"
    
    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)
    
    def formula(self):
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        
        return " ∨ ".join([Sentence().paranthesize(disjunct.formula()) for disjunct in self.disjuncts])
    
    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])
    
    def add(self, disjunct):
        Sentence().validate(disjunct)
        self.disjuncts.append(disjunct)
        return
    
    def modify(self, new_disjuncts):
        for new_disjunct in new_disjuncts:
            Sentence().validate(new_disjunct)
        self.disjuncts = list(new_disjuncts)
        return
    