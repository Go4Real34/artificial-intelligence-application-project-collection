from os import getcwd as get_current_working_directory, listdir as list_directory
from os.path import join as join_paths

from ..structures import Maze
from ..bfs_dfs_astar import BFS, DFS, ASTAR

def bfs_dfs_astar_test():
    cwd = get_current_working_directory()
    maze_folder = join_paths(cwd, 'src', 'tests', 'mazes')
    current_mazes = list_directory(maze_folder)
    
    print("Current Mazes:\n")
    for i, maze in enumerate(current_mazes):
        print(f"[{i + 1}] - {maze}")
    
    print()
    maze_index = input("Which maze do you want to solve?: ")
    print()
    try:
        if 0 < int(maze_index) <= len(current_mazes) + 1:
            maze = Maze(join_paths(maze_folder, current_mazes[int(maze_index) - 1]))
            print("[1] - BFS (Breadth First Search)")
            print("[2] - DFS (Depth First Search)")
            print("[3] - A* (A Star)")
            
            algorithm_index = input("\nWhich algorithm do you want to use?: ")
            try:
                algorithm = None
                if 0 < int(algorithm_index) <= 3:
                    if int(algorithm_index) == 1:
                        algorithm = BFS(maze)
                    elif int(algorithm_index) == 2:
                        algorithm = DFS(maze)
                    elif int(algorithm_index) == 3:
                        algorithm = ASTAR(maze)
                        
                    print()
                    
                    print("Maze:")
                    maze.print_maze()
                    
                    print("Solving started.")
                    algorithm.solve()
                    
                    print("\nNumber of nodes explored:", algorithm.number_of_explored_nodes)

                    print("\nSolution:")
                    maze.print_maze()
                        
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
    