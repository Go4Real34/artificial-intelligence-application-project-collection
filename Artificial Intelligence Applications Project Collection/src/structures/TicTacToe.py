from random import choice as random_choice

class TicTacToe:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        
        self.winner = None
        
        self.players = ['X', 'O']
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]
        
        self.available_moves = []
        for r, row in enumerate(self.board):
            for c, column in enumerate(row):
                if column == ' ':
                    self.available_moves.append((r, c))
        
        return
    
    def print_board(self):
        for row_index, row in enumerate(self.board):
            print(" ", end='')
            print(' | '.join(row))
            if row_index != 2:
                print('-----------')
                
        print("\n" * 3, end='')
        
        return
    
    def is_winner_exists(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
            
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] != ' ':
                return True
            
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        
        return False
        
    def next_turn(self):
        random_move = random_choice(self.available_moves)
        self.available_moves.remove(random_move)
        r, c = random_move
        self.board[r][c] = self.current_player
        self.current_player = self.players[(self.current_player_index + 1) % len(self.players)]
        
        return
    