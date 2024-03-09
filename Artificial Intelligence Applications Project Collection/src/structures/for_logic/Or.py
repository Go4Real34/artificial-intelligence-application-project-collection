from .Sentence import Sentence

class Or(Sentence):
    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
            
        self.disjuncts = list(disjuncts)
        return
    