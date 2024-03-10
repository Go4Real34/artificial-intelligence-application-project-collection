from ...structures import Symbol, Modelizer

class RAINY_DAY:
    def __init__(self):
        self.rain = Symbol("Rain")
        self.hagrid = Symbol("Hagrid")
        self.dumbledore = Symbol("Dumbledore")
        self.knowledge = None
        return
    
    def check_result(self):
        print(f"Current Knowledge Base: {self.knowledge.formula()}")
        model = Modelizer(self.knowledge, self.rain)
        is_knowledge_base_correct = model.check()
        if is_knowledge_base_correct:
            print("Correct knowledge base acquired.")
            
        else:
            print("Knowledge base is still missing some information.")
            
        return is_knowledge_base_correct
    