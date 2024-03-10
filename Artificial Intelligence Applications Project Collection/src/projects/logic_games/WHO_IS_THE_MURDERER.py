from ...structures import Problemizer, Symbol, Modelizer, Not

class WHO_IS_THE_MURDERER(Problemizer):
    def __init__(self):
        super().__init__()
        
        self.characters = ["Colonel Mustard", "Professor Plum", "Ms. Scarlet"]
        self.rooms = ["Ball Room", "Kitchen", "Library"]
        self.weapons = ["Knife", "Revolver", "Wrench"]
        
        self.symbols = []
        for character in self.characters:
            self.symbols.append(Symbol(character))
        
        for room in self.rooms:
            self.symbols.append(Symbol(room))
        
        for weapon in self.weapons:
            self.symbols.append(Symbol(weapon))
            
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
        print("1. One of the people is a murderer.")
        print("2. The murder is happened in one of the rooms.")
        print("3. The murder is done with a weapon.")
        print("4. Someone except Colonel Mustard was both not in kitchen and not carrying a revolver.")
        print("5. Someone except Ms. Scarlet either was not in library or was not carrying a wrench.")
        print("6. The murderer is not Professor Plum.")
        print("7. The murder is not done in Ball Room.")
        return
    
    def introduce_problem(self):
        print("Welcome to the Who Is The Murderer problem.")
        print("Result must give the murderer's name, room and weapon.")
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
                model_true = Modelizer(self.knowledge, symbol)
                model_false = Modelizer(self.knowledge, Not(symbol))
                if model_true.check():
                    correct_hits += 1
                    correct_answer.append(symbol)
                    print(f"{symbol}: Is found correct.")
                
                elif not model_false.check():
                    print(f"{symbol}: Is maybe correct.")
                
        if correct_hits == 3:
            print("\nCorrect knowledge base acquired. Well done!")
            print(f"{str(correct_answer[0])} done the murder in {str(correct_answer[1])} with a {str(correct_answer[2])}.")
        
        else:
            print("\nKnowledge base is still missing some information. Keep trying!")
            
        return correct_hits == 3
    