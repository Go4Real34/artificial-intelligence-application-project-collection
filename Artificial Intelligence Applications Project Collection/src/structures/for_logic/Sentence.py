class Sentence:
    def __init__(self):
        return
    
    def evaluate(self, model):
        raise Exception("Nothing to evaluate.")
    
    def formula(self):
        return ""
    
    def symbols(self):
        return set()
    
    def validate(self, sentence):
        if not isinstance(sentence, Sentence):
            raise TypeError("Sentence must be a logical sentence.")
        
        return
    
    def are_parantheses_balanced(self, sentence):
        count = 0
        for character in sentence:
            if character == '(':
                count += 1
                    
            elif character == ')':
                if count <= 0:
                    return False
                    
                count -= 1
                    
        return count == 0
    
    def paranthesize(self, sentence):
        if not len(sentence) or sentence.isalpha() or (sentence[0] == '(' and sentence[-1] and self.are_parantheses_balanced(sentence[1 : -1])):
            return sentence
        
        return f"({sentence})"
    