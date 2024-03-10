from ...structures import Problemizer, Symbol

class WHO_IS_THE_MURDERER(Problemizer):
    def __init__(self):
        self.characters = ["Colonel Mustard", "Professor Plum", "Ms. Scarlet"]
        self.rooms = ["Ball Room", "Kitchen", "Library"]
        self.weapons = ["Knife", "Revolver", "Wrench"]
        
        self.symbols = []
        for character in self.character:
            self.symbols.append(Symbol(character))
        
        for room in self.rooms:
            self.symbols.append(Symbol(room))
        
        for weapon in self.weapons:
            self.symbols.append(Symbol(weapon))
            
        self.operations: {
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
    