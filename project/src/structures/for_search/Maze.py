import PIL
import os

class Maze:
    def __init__(self, file_name):
        self.file_name = file_name
        file_content = self.read_and_save_file(self.file_name)
        file_content_lines = self.split_file_content_by_lines(file_content)
        self.width, self.height = self.get_maze_width_and_height(file_content_lines)
        self.start, self.goal, self.walls = self.get_maze_properties(file_content_lines)
        self.solution = None
        
        self.explored_nodes = None
        self.file_save_location = None
        
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
        maze_solution = self.solution[1] if self.solution is not None else None

        print()
        
        for rowIndex, rowValue in enumerate(self.walls):
            for columnIndex, columnValue in enumerate(rowValue):
                if (rowIndex, columnIndex) == self.start:
                    print("A", end="")
                    
                elif (rowIndex, columnIndex) == self.goal:
                    print("B", end="")
                    
                elif self.solution is not None and (rowIndex, columnIndex) in maze_solution:
                    print("*", end="")
                    
                elif columnValue:
                    print("█", end="")
                else:
                    print(" ", end="")
            
            print()
        
        print()
        
        return
    
    def set_explored_nodes(self, explored_nodes):
        self.explored_nodes = explored_nodes
        return
    
    def set_file_save_location(self, file_save_location):
        self.file_save_location = file_save_location
        return
    
    def save_maze_solution_as_file(self, used_algorithm_name):
        cell_size = 50
        cell_border = 2

        image = PIL.Image.new(
            "RGBA", 
            (self.width * cell_size, self.height * cell_size), 
            "black"
        )
        draw = PIL.ImageDraw.Draw(image)
        
        solution = self.solution[1] if self.solution is not None else None
        for r, row in enumerate(self.walls):
            for c, column in enumerate(row):
                if column:
                    fill = (40, 40, 40)
                    
                elif (r, c) == self.start:
                    fill = (255, 0, 0)
                    
                elif (r, c) == self.goal:
                    fill = (0, 171, 28)
                    
                elif solution is not None and (r, c) in solution:
                    fill = (220, 235, 113)
                    
                elif solution is not None and (r, c) in self.explored_nodes:
                    fill = (212, 97, 85)
                    
                else:
                    fill = (237, 240, 252)
                    
                draw.rectangle(
                    ([(c * cell_size + cell_border, r * cell_size + cell_border), 
                      ((c + 1) * cell_size - cell_border, (r + 1) * cell_size - cell_border)]), 
                      fill = fill
                )
                
        if (self.file_save_location is not None) or (self.explored_nodes is not None):
            file_full_save_location = os.path.join(
                self.file_save_location, 
                self.file_name.split("\\")[-1].rstrip(".txt") + "_txt_with_" + used_algorithm_name + ".png"
            )
            if os.path.exists(file_full_save_location):
                os.remove(file_full_save_location)
                
            else:
                if not os.path.exists(self.file_save_location):
                    os.makedirs(self.file_save_location)
                
            image.save(file_full_save_location)
            print("Solution saved at:", file_full_save_location)
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
            current_row = []
            for column in range(self.width):
                try:
                    if file_content_lines[row][column] == "A":
                        start = (row, column)
                        current_row.append(False)
                        
                    elif file_content_lines[row][column] == "B":
                        goal = (row, column)
                        current_row.append(False)
                        
                    elif file_content_lines[row][column] == " ":
                        current_row.append(False)
                        
                    else:
                        current_row.append(True)
                        
                except IndexError:
                    current_row.append(False)
                    
            walls.append(current_row)
            
        return start, goal, walls
    