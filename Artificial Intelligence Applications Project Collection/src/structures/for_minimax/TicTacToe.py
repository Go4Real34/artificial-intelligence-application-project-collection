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
        print("\nCurrent Board:\n")
        for row_index, row in enumerate(self.board):
            print(" ", end='')
            print(' | '.join(row))
            if row_index != 2:
                print('-----------')
        
        return
    
    def get_winner(self):
        previous_player = self.players[(self.current_player_index - 1) % len(self.players)]
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                self.winner = previous_player
            
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] != ' ':
                self.winner = previous_player
            
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = previous_player
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = previous_player
        
        if self.winner is None and len(self.available_moves) == 0:
            self.winner = "tie"
        
        return self.winner
        
    def next_turn(self, move):
        if move in self.available_moves:
            self.available_moves.remove(move)
            r, c = move
            self.board[r][c] = self.current_player
            self.current_player_index += 1
            self.current_player = self.players[self.current_player_index % len(self.players)]
        
        else:
            print('Invalid move', end='')
            print("\n" * 3, end='')

        return
    