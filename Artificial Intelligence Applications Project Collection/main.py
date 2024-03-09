from src.tests import bfs_dfs_astar_test
from src.tests import minimax_agent_test

def main():
    print("Available Tests:\n")
    
    print("[1] - BFS, DFS, ASTAR Maze Solver")
    print("[2] - Tic Tac Toe Minimaxer")
    
    test_index = input("\nWhich test you want to execute?: ")
    print()
    
    try:
        selected_index = int(test_index)
        
        if 0 < selected_index <= 3:
            if selected_index == 1:
                bfs_dfs_astar_test()
                
            elif selected_index == 2:
                minimax_agent_test()
                
        else:
            print("Invalid index.")
            exit(2)
            
    except ValueError:
        print("Invalid input.")
        exit(1)
            
    return 0


if __name__ == '__main__':
    main()
