class Maze:
    def __init__(self, file_name):
        file_content = self.read_and_save_file_content(file_name)
        file_content_lines = self.split_file_content_by_lines(file_content)
        self.width, self.height = self.get_maze_width_and_height(file_content_lines)
        self.start, self.goal, self.walls = self.get_maze_properties(file_content_lines)
        self.solution = None
        
        return
    
    def get_available_actions(self, state):
        row, column = state
        neighbors = [
            ("up", (row - 1, column)),
            ("down", (row + 1, column)),
            ("left", (row, column - 1)),
            ("right", (row, column + 1))
        ]
        
        available_actions = []
        for action, (r, c) in neighbors:
            if (0 <= r < self.height) and (0 <= c < self.width) and (not self.walls[r][c]):
                available_actions.append((action, (r, c)))
                
        return available_actions
    
    def set_solution(self, solution):
        self.solution = solution
        
        return
    
    def print_maze(self):
        print()
        for rowIndex, rowValue in enumerate(self.walls):
            for columnIndex, columnValue in enumerate(rowValue):
                if columnValue:
                    print("█", end="")
                
                elif (rowIndex, columnIndex) == self.start:
                    print("A", end="")
                    
                elif (rowIndex, columnIndex) == self.goal:
                    print("B", end="")
                    
                elif self.solution is not None and (rowIndex, columnIndex) in solution:
                    print("*", end="")
                    
                else:
                    print(" ", end="")
            
            print()
        
        print()
        
        return
    
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
    
    def get_maze_properties(self, file_content_lines):
        walls = []
        for row in range(self.height):
            row = []
            for column in range(self.width):
                try:
                    if file_content_lines[row][column] == "A":
                        start = (row, column)
                        
                    elif file_content_lines[row][column] == "B":
                        goal = (row, column)
                        
                    elif file_content_lines[row][column] == " ":
                        row.append(False)
                        
                    else:
                        row.append(True)
                        
                except IndexError:
                    row.append(False)
                    
            walls.append(row)
            
        return start, goal, walls
    