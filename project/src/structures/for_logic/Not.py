from .Sentence import Sentence

class Not(Sentence):
    def __init__(self, operand):
        Sentence().validate(operand)
        self.operand = operand
        return
    
    def __eq__(self, other):
        return (isinstance(other, Not)) and (self.operand == other.operand)
    
    def __hash__(self):
        return hash(("not", hash(self.operand)))
    
    def __repr__(self):
        return f"Not({self.operand})"
    
    def evaluate(self, model):
        return not self.operand.evaluate(model)
    
    def formula(self):
        return '¬' + Sentence().paranthesize(self.operand.formula())
    
    def symbols(self):
        return self.operand.symbols()
    
    def modify(self, new_operand):
        Sentence().validate(new_operand)
        self.operand = new_operand
        return
    