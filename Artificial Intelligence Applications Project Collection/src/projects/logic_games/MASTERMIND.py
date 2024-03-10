from ...structures import Problemizer, Symbol

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
    