class SnakesAndLadderBoard:

    def __init__(self):
        self.max = 100
        self.snake_mapping = {}
        self.ladder_mapping = {}

    def check_coordinate_availability(self, start, end):
        if self.snake_mapping.get(start, None) or self.ladder_mapping.get(start):
            print("Snake or ladder already start af that pos")
            return False
        return True

    def create_snakes(self, start, end):
        if start <= end or not self.check_coordinate_availability(start, end):
            print("Invalid input for a snake")
            return

        self.snake_mapping[start] = end
        print("snake added")
        return

    def create_ladder(self, start, end):
        if start >= end or not self.check_coordinate_availability(start, end):
            print("Invalid input for a ladder")
            return

        self.ladder_mapping[start] = end
        print("ladder added")
        return