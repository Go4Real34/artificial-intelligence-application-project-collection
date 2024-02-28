from src.tests import bfs_dfs_astar_test

def main():
    print("Available Tests:\n")
    
    print("[1] - BFS, DFS, ASTAR Maze Solver")
    
    test_index = input("\nWhich test you want to execute?: ")
    print()
    
    try:
        if 0 < int(test_index) <= 1:
            if int(test_index) == 1:
                bfs_dfs_astar_test()
            
        else:
            print("Invalid index.")
            exit(2)
            
    except ValueError:
        print("Invalid input.")
        exit(1)
            
    return 0


if __name__ == '__main__':
    main()
