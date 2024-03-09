from ...structures import TicTacToe

class MINIMAX:
    def __init__(self, game):
        self.game = game
        
        return

    def get_best_move(self, letter):
        best_score, best_move = self.minimax(self.game, letter)
        return best_move

    def minimax(self, game, player):
        if game.get_winner() == 'O':
            return 1, None
        elif game.get_winner() == 'X':
            return -1, None
        elif game.get_winner() == 'tie':
            return 0, None

        moves = []
        scores = []

        for move in game.available_moves:
            game_copy = self.copy_game(game)
            game_copy.next_turn(move)
            score, _ = self.minimax(game_copy, 'X' if player == 'O' else 'O')
            moves.append(move)
            scores.append(score)

        if player == 'O':
            best_score_index = scores.index(max(scores))
        else:
            best_score_index = scores.index(min(scores))

        return scores[best_score_index], moves[best_score_index]

    def copy_game(self, game_to_be_copied):
        copied_game = TicTacToe()
        copied_game.board = [row.copy() for row in game_to_be_copied.board]
        copied_game.winner = game_to_be_copied.winner
        copied_game.players = game_to_be_copied.players.copy()
        copied_game.current_player_index = game_to_be_copied.current_player_index
        copied_game.current_player = game_to_be_copied.current_player
        copied_game.available_moves = game_to_be_copied.available_moves.copy()
        return copied_game
    