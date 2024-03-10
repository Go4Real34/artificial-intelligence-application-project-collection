from .Symbol import Symbol
from .Modelizer import Modelizer
from .And import And
from .Or import Or
from .Not import Not
from .Implication import Implication
from .Biconditional import Biconditional

class Problemizer:
    def __init__(self):
        self.operations = None
        self.operands = None
        
        self.knowledge = And()
        self.knowledge_length = 0
        
        return
    
    def introduce_problem(self):
        raise Exception("No problem exists.")
        return
    
    def get_information(self):
        print("\nSelect a logical operation.")
        for key, value in self.operations.items():
            print(f"[{key}] - {value}")
        print(f"[{len(self.operations) + 1}] - Clear Knowledge Base")
        print(f"[{len(self.operations) + 2}] - Clear Extra Added Operands")
        
        logical_operation = input("Enter the number of the logical operation: ").rstrip().lstrip()
        if logical_operation == "":
            print("No logical operation selected.")
            exit(2)
            
        selected_operation_index = None
        try:
            selected_operation_index = int(logical_operation)
            if selected_operation_index == len(self.operations) + 1:
                return selected_operation_index, [0], True
            
            elif selected_operation_index == len(self.operations) + 2:
                return selected_operation_index, [0], False
            
            if not (0 < selected_operation_index <= len(self.operations)):
                print("Invalid index on logical operation selection.")
                exit(2)
                
        except ValueError:
            print("Invalid input type on logical operation selection.")
            exit(2)
            
        print("\nSelect the operand." if self.operations[selected_operation_index] == "Not" else "\nSelect the operands.")
        for key, value in self.operands.items():
            print(f"[{key}] - {value[0]}")
            
        operand_s = input("Enter the numbers of operands: ").rstrip().lstrip()
        if operand_s == "":
            print("No operands selected.")
            exit(2)
            
        selected_operand_indexes = None
        try:
            operands = [int(operand) for operand in operand_s.split(" ")]
            if self.operations[selected_operation_index] == "Not" and len(operands) != 1:
                print("Invalid number of operands for Not operation.")
                exit(2)
                
            elif self.operations[selected_operation_index] == "Implication" and len(operands) != 2:
                print("Invalid number of operands for Implication operation.")
                exit(2)
                
            elif self.operations[selected_operation_index] == "Biconditional" and len(operands) != 2:
                print("Invalid number of operands for Biconditional operation.")
                exit(2)
                
            else:
                selected_operand_indexes = operands
                
        except ValueError:
            print("Invalid input type on operand selection.")
            exit(2)
            
        print("\nSelect the place to save this statement.")
        print(f"[1] - Save in the knowledge base.")
        print(f"[2] - Save it as an operand.")
        
        place = input("Enter the number of the place to save the statement: ").rstrip().lstrip()
        if place == "":
            print("No place selected.")
            exit(2)
            
        selected_place_index = None
        try:
            selected_place_index = int(place)
            if not (0 < selected_place_index <= 2):
                print("Invalid index on place selection.")
                exit(2)
                
        except ValueError:
            print("Invalid input type on place selection.")
            exit(2)
            
        return selected_operation_index, selected_operand_indexes, (selected_place_index == 1)

    def add_information(self):
        operation_index, operands_index, should_save_to_knowledge_base = self.get_information()
        if operation_index == len(self.operations) + 1 and operands_index == [0] and should_save_to_knowledge_base:
            self.clear_knowledge_base()
            print("\nKnowledge base is cleared.")
            return
        
        if operation_index == len(self.operations) + 2 and operands_index == [0] and not should_save_to_knowledge_base:
            self.clear_extra_added_operands()
            print("\nExtra Added Operands are cleared.")
            return
        
        thing_to_add = None
        if self.operations[operation_index] == "Not":
            thing_to_add = Not(self.operands[operands_index[0]][1])
            
        elif self.operations[operation_index] == "Implication":
            thing_to_add = Implication(self.operands[operands_index[0]][1], self.operands[operands_index[1]][1])
            
        elif self.operations[operation_index] == "Biconditional":
            thing_to_add = Biconditional(self.operands[operands_index[0]][1], self.operands[operands_index[1]][1])
            
        elif self.operations[operation_index] == "Or":
            or_statement = Or()
            for operand in operands_index:
                or_statement.add(self.operands[operand][1])  
            thing_to_add = or_statement
            
        elif self.operations[operation_index] == "And":
            and_statement = And()
            for operand in operands_index:
                and_statement.add(self.operands[operand][1])  
            thing_to_add = and_statement
            
        self.operands.update({len(self.operands) + 1: [thing_to_add.formula(), thing_to_add]})
        if should_save_to_knowledge_base:
            self.knowledge.add(thing_to_add)
            self.knowledge_length += 1
        
        return
    
    def clear_knowledge_base(self):
        self.knowledge = And()
        self.knowledge_length = 0
        return
    
    def clear_extra_added_operands(self):
        raise Exception("No extra added knowledge exists.")
    
    def check_result(self):
        print(f"\nCurrent Knowledge Base: " + (f"{self.knowledge.formula()}" if self.knowledge_length != 0 else "None"), end='\n' * 2)
        
        if self.knowledge_length != 0:
            model = Modelizer(self.knowledge, self.rain)
            is_knowledge_base_correct = model.check()
            if is_knowledge_base_correct:
                print("Correct knowledge base acquired. Well done!")
            
            else:
                print("Knowledge base is still missing some information. Keep trying!")
                
            return is_knowledge_base_correct
            
        return False
    