from ...structures import Problemizer, Symbol, Modelizer

class MASTERMIND(Problemizer):
    def __init__(self):
        super().__init__()
        
        self.colors = ["Red", "Blue", "Green", "Yellow"]
        self.positions = [1, 2, 3, 4]
        self.symbols = []
        for position in range(4):
            for color in self.colors:
                for position in self.positions:
                    self.symbols.append(Symbol(f"{color} {position}"))
                
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
    
    def print_problem_information(self):
        print("\t1. Each color has a position.")
        print("\t2. Only one position can hold a color.")
        print("\t3. Only one color can be at a position.")
        print("\t4. If Red is at Position 1, Blue can be at Position 2; but neither Green can be at Position 3 nor Yellow can be at Position 4.")
        print("\t5. If Red is at Position 1, Green can be at Position 3; but neither Blue can be at Position 2 nor Yellow can be at Position 4.")
        print("\t6. If Red is at Position 1, Yellow can be at Position 4; but neither Blue can be at Position 2 nor Green can be at Position 3.")
        print("\t7. If Blue is at Position 2, Green can be at Position 3; but neither Red can be at Position 1 nor Yellow can be at Position 4.")
        print("\t8. If Blue is at Position 2, Yellow can be at Position 4; but neither Red can be at Position 1 nor Green can be at Position 3.")
        print("\t9. If Green is at Position 3, Yellow can be at Position 4; but neither Red can be at Positio n1 nor Blue can be at Position 2.")
        print("\t10. Either one or all of the statements 4, 5, 6, 7, 8 and 9 are true.")
        print("\t11. Blue cannot be at Position 1.")
        print("\t12. Red cannot be at Position 2.")
        print("\t13. Green cannot be at Position 3.")
        print("\t14. Yellow cannot be at Position 4.")
        return
    
    def introduce_problem(self):
        print("Welcome to the Mastermind problem.")
        print("Result must give correct positions of the colors.")
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
                color, position = str(answer).split(" ")
                print(f"{color} is at position {position}.")
            
        else:
            print("Knowledge base is still missing some information. Keep trying!")
            
        return (correct_hits == 4)
    