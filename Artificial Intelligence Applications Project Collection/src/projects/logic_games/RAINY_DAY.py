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
            5: "Biconditional",
            6: "Add Knowledge to Knowledge Base from Extra Added Operands",
            7: "Clear Knowledge Base",
            8: "Clear Extra Added Operands"
        }
        
        self.operands = {
            1: ["Rain", self.rain],
            2: ["Hagrid", self.hagrid],
            3: ["Dumbledore", self.dumbledore]
        }
    
    def play(self):
        self.introduce_problem()
        while True:
            self.print_problem_information()
            self.add_information()
            if self.check_result(self.knowledge, self.rain):
                break
            
        return
    
    def print_problem_information(self):
        print("\t1. If it is not raining, Hagrid will be happy.")
        print("\t2. Either Hagrid or Dumbledore is happy.")
        print("\t3. But Hagrid and Dumbledore cannot be sad at the same time.")
        print("\t4. And Dumbledore must be happy.")
        return
    
    def introduce_problem(self):
        print("Welcome to the rainy day problem.")
        print("Result must give 'Yes' answer to the question 'Is it raining?'")
        print("Create the correct knowledge base to solve the problem.")
        print("The problem is as follows:")
        return
    
    def clear_extra_added_operands(self):
        self.operands = {
            1: ["Rain", self.rain],
            2: ["Hagrid", self.hagrid],
            3: ["Dumbledore", self.dumbledore]
        }
        
        return
    