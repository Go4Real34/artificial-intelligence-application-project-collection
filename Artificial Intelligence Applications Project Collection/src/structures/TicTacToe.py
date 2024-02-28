class TicTacToe:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        
    def print_board(self):
        for row_index, row in enumerate(self.board):
            print('|'.join(row))
            if row_index != 2:
                print('-----')
                
        print()
        
        return
    