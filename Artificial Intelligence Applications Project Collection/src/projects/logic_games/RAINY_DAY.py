from ...structures import Problemizer, Symbol, Modelizer, And, Or, Not, Implication, Biconditional

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
    
    def add_information(self):
        operation_index, operands_index, should_save_to_knowledge_base = self.get_information()
        if operation_index == len(self.operations) - 2 and operands_index != [0] and should_save_to_knowledge_base:
            self.knowledge.add(self.operands[operands_index[0]][1])
            self.knowledge_length += 1
            return

        elif operation_index == len(self.operations) - 1 and operands_index == [0] and should_save_to_knowledge_base:
            self.clear_knowledge_base()
            print("\nKnowledge base is cleared.")
            return
        
        elif operation_index == len(self.operations) and operands_index == [0] and not should_save_to_knowledge_base:
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
    
    def clear_extra_added_operands(self):
        self.operands = {
            1: ["Rain", self.rain],
            2: ["Hagrid", self.hagrid],
            3: ["Dumbledore", self.dumbledore]
        }
        
        return
    
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