import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())
        return self.minimax(game, self.letter)['position']

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score': (state.num_empty_squares() + 1) * (-1 if other_player == max_player else 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        best = {'position': None, 'score': -math.inf if player == max_player else math.inf}
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            state.undo_move(possible_move)

            sim_score['position'] = possible_move

            if (player == max_player and sim_score['score'] > best['score']) or (
                    player != max_player and sim_score['score'] < best['score']):
                best = sim_score

        return best


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input('')  # front end code
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
