from ...structures import Symbol, Modelizer

class RAINY_DAY:
    def __init__(self):
        self.rain = Symbol("Rain")
        self.hagrid = Symbol("Hagrid")
        self.dumbledore = Symbol("Dumbledore")
        self.knowledge = None
        return
    
    def introduce_problem(self):
        print("Welcome to the rainy day problem.")
        print("The problem is as follows:")
        print("If it is not raining, Hagrid will be happy.")
        print("Either Hagrid or Dumbledore is happy.")
        print("But Hagrid and Dumbledore cannot be sad at the same time.")
        print("Create the correct knowledge base to solve the problem.")
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
    