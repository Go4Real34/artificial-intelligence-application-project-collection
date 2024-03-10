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
            6: "Add Knowledge to Knowledge Base from Extra Added Operands",
            7: "Clear Knowledge Base",
            8: "Clear Extra Added Operands"
        }
        
        self.operands = {}
        for index, symbol in enumerate(self.symbols):
            self.operands.update({
                index + 1: [symbol.formula(), symbol]
            })
            
        return
    
    def clear_extra_added_operands(self):
        self.operands = {}
        for index, symbol in enumerate(self.symbols):
            self.operands.update({
                index + 1: [symbol.formula(), symbol]
            })
            
        return
    