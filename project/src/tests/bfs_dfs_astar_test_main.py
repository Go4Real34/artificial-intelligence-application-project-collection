import os

from ..structures import Maze
from ..projects import BFS, DFS, ASTAR

def bfs_dfs_astar_test():
    cwd = os.getcwd()
    mazes_folder = os.path.join(cwd, "src", "tests", "mazes")
    current_mazes = os.listdir(mazes_folder)
    
    print("Current Mazes:\n")
    for i, maze in enumerate([maze for maze in current_mazes if maze.endswith(".txt")]):
        print(f"[{i + 1}] - {maze}")
    
    print()
    maze_index = input("Which maze do you want to solve?: ")
    print()
    try:
        if 0 < int(maze_index) <= len(current_mazes) + 1:
            maze_file_name = current_mazes[int(maze_index) - 1]
            maze_file_path = os.path.join(mazes_folder, maze_file_name)
            maze = Maze(maze_file_path)
            
            algorithms = [
                "[1] - BFS (Breadth First Search)",
                "[2] - DFS (Depth First Search)",
                "[3] - A* (A Star)"
            ]
            
            for algorithm in algorithms:
                print(algorithm)
                
            algorithm_index = input("\nWhich algorithm do you want to use?: ")
            try:
                algorithm = None
                algorithm_name = None
                if 0 < int(algorithm_index) <= len(algorithms):
                    if int(algorithm_index) == 1:
                        algorithm = BFS(maze)
                        algorithm_name = "bfs"
                    elif int(algorithm_index) == 2:
                        algorithm = DFS(maze)
                        algorithm_name = "dfs"
                    elif int(algorithm_index) == 3:
                        algorithm = ASTAR(maze)
                        algorithm_name = "astar"
                        
                    print()
                    
                    print("Maze:")
                    maze.print_maze()
                    
                    print("Solving started.")
                    algorithm.solve()
                    maze.set_explored_nodes(algorithm.explored_nodes)
                    
                    print("\nNumber of nodes explored:", algorithm.number_of_explored_nodes)

                    print("\nSolution:")
                    maze.print_maze()
                    
                    maze.set_file_save_location(os.path.join(mazes_folder, "solutions", maze_file_name.rstrip(".txt")))
                    maze.save_maze_solution_as_file(algorithm_name)
                        
                else:
                    print("Invalid index on algorithm selection.")
                    exit(2)
                    
            except ValueError:
                print("Invalid input type on algorithm selection.")
                exit(1)
        else:
            print("Non-existent algorithm selection.")
            exit(2)
    
    except ValueError:
        print("Invalid input type on maze selection.")
        exit(1)


def main():
    return 0


if __name__ == '__main__':
    main()
    