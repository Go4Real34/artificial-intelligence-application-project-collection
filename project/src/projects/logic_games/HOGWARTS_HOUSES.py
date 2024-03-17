from ...structures import Problemizer, Symbol, Modelizer

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
            6: "Add Knowledge to Knowledge Base from Extra Added Operands",
            7: "Clear Knowledge Base",
            8: "Clear Extra Added Operands"
        }
        
        self.operands = {}
        for index, symbol in enumerate(self.symbols):
            self.operands.update({
                index + 1: [str(symbol), symbol]
            })
            
        return
    
    def play(self):
        self.introduce_problem()
        while True:
            self.print_problem_information()
            self.add_information()
            if self.check_result():
                break
            
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
        print("Welcome to the Hogwart's Houses Problem.")
        print("Result must give the house of each person.")
        print("Create the correct knowledge base to solve the problem.")
        print("The problem is as follows:")
        return
    
    def add_information(self):
        operation_index, operands_index, should_save_to_knowledge_base = self.get_information()
        self.add_logical_expression_to_knowledge_base(operation_index, operands_index, should_save_to_knowledge_base)
        return
    
    def clear_extra_added_operands(self):
        self.operands = {}
        for index, symbol in enumerate(self.symbols):
            self.operands.update({
                index + 1: [str(symbol), symbol]
            })
            
        return
    
    def check_result(self):
        print(f"\nCurrent Knowledge Base: " + (f"{self.knowledge.formula()}" if self.knowledge_length != 0 else "None"), end='\n' * 2)
        
        correct_hits = 0
        correct_answer = []
        if self.knowledge_length != 0:
            for symbol in self.symbols:
                model = Modelizer(self.knowledge, symbol)
                if model.check():
                    correct_hits += 1
                    correct_answer.append(symbol)
                    print(f"{str(symbol)} is correct.")
                    
        if correct_hits == 4:
            print("Correct knowledge base is acquired. Well done!")
            for answer in correct_answer:
                person, house = str(answer).split(" ")
                print(f"{person} belongs to {house}.")
                
        else:
            print("Knowledge base is still missing some information. Keep trying!")
        
        return (correct_hits == 4)
    