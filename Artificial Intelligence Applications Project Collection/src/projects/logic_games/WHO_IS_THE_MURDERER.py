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
    