from src.tests import bfs_dfs_astar_test
from src.tests import minimax_agent_test
from src.tests import logic_games_test
from src.tests import turkish_banksnotes_fraud_detection_test

def main():
    print("Available Tests:\n")
    
    tests = [
        "[1] - BFS, DFS, ASTAR Maze Solver", 
        "[2] - Tic Tac Toe Minimaxer",
        "[3] - Logic Games",
        "[4] - Turkish Banknotes Fraud Detection"
    ]
    
    for test in tests:
        print(test)
        
    test_index = input("\nWhich test you want to execute?: ")
    print()
    
    try:
        selected_index = int(test_index)
        
        if 0 < selected_index <= len(tests):
            if selected_index == 1:
                bfs_dfs_astar_test()
                
            elif selected_index == 2:
                minimax_agent_test()
                
            elif selected_index == 3:
                logic_games_test()
                
            elif selected_index == 4:
                turkish_banksnotes_fraud_detection_test()
                
        else:
            print("Invalid index on test selection.")
            exit(2)
            
    except ValueError:
        print("Invalid input on test selection.")
        exit(1)
            
    return 0


if __name__ == '__main__':
    main()
