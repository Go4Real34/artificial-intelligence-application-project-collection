from .Sentence import Sentence

class Or(Sentence):
    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
            
        self.disjuncts = list(disjuncts)
        return
    
    def __eq__(self, other):
        return (isinstance(other, Or)) and self.disjuncts == other.disjuncts
    
    def __hash__(self):
        return hash(("or", tuple(hash(disjunct) for disjunct in self.disjuncts)))
    
    def __repr__(self):
        disjunts = ", ".join([str(disjunct) for disjunct in self.disjuncts])
        return f"Or({disjunts})"
    