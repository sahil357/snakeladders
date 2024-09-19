import random
from players import Player
from board import SnakesAndLadderBoard
class Game:

    def __init__(self, snake_ladder_board):
        self.board = snake_ladder_board
        self.player_mapping = {}
        self.player_position = {}
        self.status = 'Initiated'
        self.winner = None
        self.current_player = None
        self.pause = True

    def roll_dice(self):
        return random.randint(1, 7)

    def add_player(self, name, code):
        if self.player_mapping.get(code, None):
            print("player code already exist, try something else")
            return
        player = Player(name, code)
        self.player_mapping[code] = player
        self.player_position[code] = 0

    def get_player_position(self, current_position, dice_roll):
        new_position = current_position + dice_roll

        if new_position > self.board.max:
            return current_position
        while self.board.snake_mapping.get(new_position, None) or self.board.ladder_mapping.get(new_position, None):
            if self.board.snake_mapping.get(new_position, None):
                print("Got bit by a snake at {}".format(new_position))
                new_position = self.board.snake_mapping[new_position]

            if self.board.ladder_mapping.get(new_position, None):
                print("crimbing a ladder at {}".format(new_position))
                new_position = self.board.ladder_mapping[new_position]

        return new_position

    def get_player_name(self, code):
        return self.player_mapping.get(code).name

    def start_game(self):
        if self.status == 'Over':
            print("Game already over, winner - {}".format(self.winner))

        if self.status == 'Initiated':
            self.status = 'started'

        player_listing = list(self.player_mapping.keys())
        print('player_listing ', player_listing)
        total_player = len(player_listing)

        if self.current_player == None:
            self.current_player = 0

        while self.status == 'started':
            player_code = player_listing[self.current_player]
            dice_roll = self.roll_dice()
            player_position = self.player_position.get(player_code)

            if player_position > 50 and self.pause:
                self.pause = False
                self.pause_game()
                self.resume_game()
            player_new_position = self.get_player_position(player_position, dice_roll)
            self.player_position[player_code] = player_new_position
            player_code = player_listing[self.current_player]
            print("{} rolled a {} and moved from {} to {}".format(self.get_player_name(player_code), dice_roll, player_position, player_new_position))
            if player_new_position == 100:
                self.winner = player_listing[self.current_player]
                self.status = 'Over'
                print("{} wins the game".format(self.get_player_name(player_code)))
                return
            self.current_player = (self.current_player + 1) % total_player
            # print("self."self.current_player)

    def pause_game(self):
        print("game is paused")
        self.status = 'paused'
        return

    def resume_game(self):
        print('resume game')
        self.status = 'started'
        self.start_game()
        return








