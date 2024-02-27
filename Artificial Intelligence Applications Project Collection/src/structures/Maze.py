class Maze:
    def __init__(self, file_name):
        file_content = self.read_and_save_file_content(file_name)
        file_content_lines = self.split_file_content_by_lines(file_content)
        self.width, self.height = self.get_maze_width_and_height(file_content_lines)
    
    def read_and_save_file(self, file_name):
        with open(file_name) as file:
            file_content = file.read().upper()
            
        if file_content.count("A") != 1:
            raise Exception("Maze is invalid: There must be exactly one starting point!")
        
        if file_content.count("B") != 1:
            raise Exception("Maze is invalid: There must be exactly one goal!")
        
        return file_content
    
    def split_file_content_by_lines(self, file_content):
        return file_content.splitlines()
    
    def get_maze_width_and_height(self, file_content_lines):
        width = max(len(line) for line in file_content_lines)
        height = len(file_content_lines)
        
        return width, height
    