class MODELIZER:
    def __init__(self, knowledge, query):
        self.knowledge = knowledge
        self.query = query
        return
    
    def check_all(self, symbols, model):
        if not symbols:
            if self.knowledge.evaluate(model):
                return self.query.evaluate(model)
            
            return True
        
        else:
            remaining = symbols.copy()
            popped = remaining.pop()
            
            model_true = model.copy()
            model_true[popped] = True
            
            model_false = model.copy()
            model_false[popped] = False
            
            return ((self.check_all(remaining, model_true)) and (self.check_all(remaining, model_false)))
        
    def get_all_symbols_combined(self):
        return set.union(self.knowledge.symbols(), self.query.symbols())
    
    def check(self):
        symbols = self.get_all_symbols_combined()
        return self.check_all(symbols, dict())
    