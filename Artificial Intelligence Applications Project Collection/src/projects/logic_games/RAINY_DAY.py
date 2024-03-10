from ...structures import Problemizer, Symbol

class RAINY_DAY(Problemizer):
    def __init__(self):
        super().__init__()
        
        self.rain = Symbol("Rain")
        self.hagrid = Symbol("Hagrid")
        self.dumbledore = Symbol("Dumbledore")
    
        self.operations = {
            1: "And",
            2: "Or",
            3: "Not",
            4: "Implication",
            5: "Biconditional"
        }
    
        self.operands = {
            1: ["Rain", self.rain],
            2: ["Hagrid", self.hagrid],
            3: ["Dumbledore", self.dumbledore]
        }
    
    def print_problem_information(self):
        print("1 - If it is not raining, Hagrid will be happy.")
        print("2 - Either Hagrid or Dumbledore is happy.")
        print("3 - But Hagrid and Dumbledore cannot be sad at the same time.")
        print("4 - And Dumbledore must be happy.")
        return
    
    def introduce_problem(self):
        print("Welcome to the rainy day problem.")
        print("Create the correct knowledge base to solve the problem.")
        print("The problem is as follows:")
        return
    