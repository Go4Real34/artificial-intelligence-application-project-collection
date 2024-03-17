from ...structures import Problemizer, Symbol, Modelizer, And, Or, Not, Implication, Biconditional

class RAINY_DAY(Problemizer):
    def __init__(self):
        super().__init__()
        
        self.elements = ["Rain", "Hagrid", "Dumbledore"]
    
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
        for index, element in enumerate(self.elements):
            self.operands.update({
                index + 1: [element, Symbol(element)]
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
        print("\t1. If it is not raining, Hagrid will be happy.")
        print("\t2. Either Hagrid or Dumbledore is happy.")
        print("\t3. But Hagrid and Dumbledore cannot be happy at the same time.")
        print("\t4. And Dumbledore must be happy.")
        return
    
    def introduce_problem(self):
        print("Welcome to the Rainy Day Problem.")
        print("Result must give 'Yes' answer to the question 'Is it raining?'")
        print("Create the correct knowledge base to solve the problem.")
        print("The problem is as follows:")
        return
    
    def add_information(self):
        operation_index, operands_index, should_save_to_knowledge_base = self.get_information()
        self.add_logical_expression_to_knowledge_base(operation_index, operands_index, should_save_to_knowledge_base)
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
            model = Modelizer(self.knowledge, self.operands[1][1])
            is_knowledge_base_correct = model.check()
            if is_knowledge_base_correct:
                print("Correct knowledge base is acquired. Well done!")
                print("It is raining, so Hagrid is not happy but Dumbledore is happy. With that both of them is not happy at the same time sad. So, the result is 'Yes'.")
            
            else:
                print("Knowledge base is still missing some information. Keep trying!")
                
            return (is_knowledge_base_correct)
            
        return False
    