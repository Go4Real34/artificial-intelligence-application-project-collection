from ...structures import Symbol, Modelizer, And, Or, Not, Implication, Biconditional

class RAINY_DAY:
    def __init__(self):
        self.rain = Symbol("Rain")
        self.hagrid = Symbol("Hagrid")
        self.dumbledore = Symbol("Dumbledore")
        self.knowledge = And()
        
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
        
        return
    
    def introduce_problem(self):
        print("Welcome to the rainy day problem.")
        print("The problem is as follows:")
        print("If it is not raining, Hagrid will be happy.")
        print("Either Hagrid or Dumbledore is happy.")
        print("But Hagrid and Dumbledore cannot be sad at the same time.")
        print("Create the correct knowledge base to solve the problem.")
        return
    
    def get_information(self):
        print("Select a logical operation.")
        for key, value in self.operations.items():
            print(f"[{key}] - {value}")
        
        logical_operation = input("Enter the number of the logical operation: ").rstrip()
        if logical_operation == "":
            print("No logical operation selected.")
            exit(2)
            
        selected_operation_index = None
        try:
            selected_operation_index = int(logical_operation)
            if not (0 < selected_operation_index <= len(self.operations)):
                print("Invalid index on logical operation selection.")
                exit(2)
                
        except ValueError:
            print("Invalid input type on logical operation selection.")
            exit(2)
            
        print("Select the operand." if self.operations[selected_operation_index] == "Not" else "Select the operands.")
        for key, value in self.operands.items():
            print(f"[{key}] - {value[0]}")
            
        operand_s = input("Enter the numbers of operands: ").rstrip()
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
            
        return selected_operation_index, selected_operand_indexes

    def add_information(self):
        operation, operands = self.get_information()
        if self.operations[operation] == "Not":
            self.knowledge.add(Not(self.operands[operands[0]][1]))
            
        elif self.operations[operation] == "Implication":
            self.knowledge.add(Implication(self.operands[operands[0]][1], self.operands[operands[1]][1]))
            
        elif self.operations[operation] == "Biconditional":
            self.knowledge.add(Biconditional(self.operands[operands[0]][1], self.operands[operands[1]][1]))
            
        elif self.operations[operation] == "Or":
            or_statement = Or()
            for operand in operands:
                or_statement.add(self.operands[operand][1])  
            self.knowledge.add(or_statement)
            
        elif self.operations[operation] == "And":
            and_statement = And()
            for operand in operands:
                and_statement.add(self.operands[operand][1])  
            self.knowledge.add(and_statement)
            
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
    