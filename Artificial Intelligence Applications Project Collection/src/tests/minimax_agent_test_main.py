from ..structures import TicTacToe
from ..minimax_agent import MINIMAX

def minimax_agent_test():
    game = TicTacToe()
    
    try:
        player = input("Which player do you want to be? [First character will be saved as answer!] (X or O): ").rstrip().lstrip().upper()[0]
    
    except IndexError:
        print('Empty input on player selection.')
        exit(1)
        
    if player != 'X' and player != 'O':
        print('Non-existent player selection.')
        exit(1)
        
    else:
        try:
            first_or_second = input("Do you want to go first or second? [First character will be saved as answer!] (F or S): ").rstrip().lstrip().upper()[0]
            
        except IndexError:
            print('Empty input on order selection.')
            exit(1)
            
        if first_or_second != 'F' and first_or_second != 'S':
            print('Non-existent order selection.')
            exit(1)
            
        else:
            if first_or_second == 'F':
                game.current_player = player
            else:
                game.current_player = 'X' if player == 'O' else 'O'
                
            game.current_player_index = 0 if game.current_player == 'X' else 1
                
        
        
    while True:
        game.print_board()
        winner = game.get_winner()
        if winner == 'X' or winner == 'O':
            print(f'\n{winner} wins!\n')
            break
        
        elif game.winner == 'tie':
            print("\nTie!\n")
            break
        
        if game.current_player == player:
            print("\nPlayer's turn.\n")
            try:
                position_input = input('Enter row and column with one space [Ex: 1 1]: ').rstrip().lstrip().split(" ")
                
            except IndexError:
                print("Empty input on position selection.")
                exit(1)
                
            try:
                row, column = int(position_input[0]) - 1, int(position_input[1]) - 1
                if row < 0 or row > 3:
                    print("Invalid row interval.")
                    exit(2)
                    
                if row < 0 or row > 3:
                    print("Invalid column interval.")
                    exit(2)
            
            except ValueError:
                print("Invalid row and column type.")
                exit(1)
                
            except IndexError:
                print("Missing row or column input.")
                exit(1)
                
            game.next_turn((row, column))
        
        else:
            print("\nAgent's turn.\n")
            minimax = MINIMAX(game)
            agent_player_letter = 'X' if player == 'O' else 'O'
            row, column = minimax.get_best_move(agent_player_letter)
        
            game.next_turn((row, column))
            
    return 0

def main():
    return 0

if __name__ == '__main__':
    main()
    