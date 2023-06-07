import math

class Computer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game_state):
        """
        Returns the best move for the computer using the minimax algorithm.
        game_state: Current state of the game as a list.
        """
        best_move = self.minimax(game_state, self.letter)
        return best_move['position']

    def minimax(self, game_state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if self.is_winner(game_state, other_player):
            return {'position': None,
                    'score': (self.num_empty_squares(game_state) + 1) * (-1 if other_player == max_player else 1)}
        elif not self.num_empty_squares(game_state):
            return {'position': None, 'score': 0}

        best = {'position': None, 'score': -math.inf if player == max_player else math.inf}
        for possible_move in self.available_moves(game_state):
            game_state[possible_move] = player
            sim_score = self.minimax(game_state, other_player)
            game_state[possible_move] = ''  # Undo the move

            sim_score['position'] = possible_move

            if (player == max_player and sim_score['score'] > best['score']) or (
                    player != max_player and sim_score['score'] < best['score']):
                best = sim_score

        return best

    def is_winner(self, game_state, player):
        winning_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for condition in winning_conditions:
            if game_state[condition[0]] == game_state[condition[1]] == game_state[condition[2]] == player:
                return True
        return False

    def num_empty_squares(self, game_state):
        return game_state.count('')

    def available_moves(self, game_state):
        return [i for i in range(len(game_state)) if game_state[i] == '']
