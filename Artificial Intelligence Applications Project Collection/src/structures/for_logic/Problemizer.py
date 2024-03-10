from .And import And

class Problemizer:
    def __init__(self):
        self.operations = None
        self.operands = None
        
        self.knowledge = And()
        self.knowledge_length = 0
        
        return
    
    def get_information(self):
        print("\nSelect a logical operation.")
        for key, value in self.operations.items():
            print(f"[{key}] - {value}")
        
        logical_operation = input("Enter the number of the logical operation: ").rstrip().lstrip()
        if logical_operation == "":
            print("No logical operation selected.")
            exit(2)
            
        selected_operation_index = None
        try:
            selected_operation_index = int(logical_operation)
            if selected_operation_index == len(self.operations) - 1:
                return selected_operation_index, [0], True
            
            elif selected_operation_index == len(self.operations):
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
            
        operand_s = input("Enter the numbers of operands: " if self.operations[selected_operation_index] != "Not" else "Enter the number of operand: ").rstrip().lstrip()
        if operand_s == "":
            print("No operands selected." if self.operations[selected_operation_index] != "Not" else "No operand selected.")
            exit(2)
            
        selected_operand_indexes = None
        try:
            operands = [int(operand) for operand in operand_s.split(" ")]
            if selected_operation_index == len(self.operations) - 2 and len(operands) != 1:
                print("You can only select one operand to add directly to the knowledge base.")
                exit(2)
                
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
            
        if selected_operation_index == len(self.operations) - 2:
            return selected_operation_index, selected_operand_indexes, True
        
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
    
    def clear_knowledge_base(self):
        self.knowledge = And()
        self.knowledge_length = 0
        return
    