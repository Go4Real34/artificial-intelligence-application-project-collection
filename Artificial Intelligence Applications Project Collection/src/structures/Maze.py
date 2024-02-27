class Maze:
    def __init__(self, file_name):
        file_content = self.read_and_save_file_content(file_name)
    
    def read_and_save_file(self, file_name):
        with open(file_name) as file:
            file_content = file.read().upper()
            
        if file_content.count("A") != 1:
            raise Exception("Maze is invalid: There must be exactly one starting point!")
        
        if file_content.count("B") != 1:
            raise Exception("Maze is invalid: There must be exactly one goal!")
        
        return file_content
    