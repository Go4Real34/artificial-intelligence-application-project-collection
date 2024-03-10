from ...structures import Problemizer, Symbol

class HOGWARTS_HOUSES(Problemizer):
    def __init__(self):
        super().__init__()
        
        self.people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        self.symbols = []
        for people in self.people:
            for house in self.houses:
                self.symbols.append(Symbol(f"{people} {house}"))
                
        self.operations = {
            1: "And",
            2: "Or",
            3: "Not",
            4: "Implication",
            5: "Biconditional",
            7: "Add Knowledge to Knowledge Base from Extra Added Operands",
            8: "Clear Knowledge Base",
            9: "Clear Extra Added Operands"
        }
        
        self.operands = {}
        for index, symbol in enumerate(self.symbols):
            self.operands.update({
                index + 1: [str(symbol), symbol]
            })
            
        return
    
    def print_problem_information(self):
        print("\t1. Each person belongs to a house.")
        print("\t2. Only one person can belong per house.")
        print("\t3. Only one house can be belonged per person.")
        print("\t4. Gilderoy belongs to either Gryffindor or Ravenclaw.")
        print("\t5. Pomona does not belong to Slytherin.")
        print("\t6. Minerva belongs to Gryffindor.")
        return
    
    def introduce_problem(self):
        print("Welcome to the Hogwart's Houses problem.")
        print("Result must give the house of each person.")
        print("Create the correct knowledge base to solve the problem.")
        print("The problem is as follows:")
        return
    
    def clear_extra_added_operands(self):
        self.operands = {}
        for index, person in enumerate(self.people):
            self.operands.update({
                index + 1: [person, Symbol(person)]
            })
            
        return
    