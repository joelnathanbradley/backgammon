from src.Board import Board
import random


class Game:

    def __init__(self, checker_color1, checker_color2):
        self.board = Board(checker_color1, checker_color2)
        self.player1 = checker_color1
        self.player2 = checker_color2
        self.turn = self.player1
        self.dice = [0, 0]

    def first_roll(self):
        input("Press enter to determine initial roll ...")
        checker_color1_roll = 0
        checker_color2_roll = 0
        while checker_color1_roll == checker_color2_roll:
            checker_color1_roll = random.randint(1, 6)
            checker_color2_roll = random.randint(1, 6)
        self.dice = [checker_color1_roll, checker_color2_roll]
        if checker_color2_roll > checker_color1_roll:
            self.turn = self.player2

    def roll(self):
        print(self)
        input("Press enter to roll ...")
        self.dice = [random.randint(1, 6), random.randint(1, 6)]
        if self.dice[0] == self.dice[1]:
            self.dice.append(self.dice[0])
            self.dice.append(self.dice[0])

    def _get_user_input(self):
        roll = -1
        point = -1
        valid_roll = False
        valid_point = False
        while not valid_roll:
            roll = input("Enter a dice roll: ")
            if not roll.isdigit():
                print("Roll needs to be a digit.")
                continue
            roll = int(roll)
            if roll not in self.dice:
                print("Roll needs to match a dice roll.")
                continue
            valid_roll = True
        while not valid_point:
            point = input("Enter a point number: ")
            if not point.isdigit():
                print("Point needs to be a digit.")
                continue
            point = int(point)
            if point < 0 or point > 23:
                print("Point needs to be between 0 and 23.")
                continue
            if not self.board.can_move(self.turn, point, roll):
                print("Cannot move checker at this point.")
                continue
            valid_point = True
        return point, roll

    def toggle_turn(self):
        if self.turn == self.player1:
            self.turn = self.player2
        else:
            self.turn = self.player1

    def move(self):
        for _ in range(2):
            print(self)
            point, roll = self._get_user_input()
            self.board.move(self.turn, point, roll)
            self.dice.remove(roll)

    def play(self):
        self.first_roll()
        self.move()
        while not self.board.is_winner(self.turn):
            self.toggle_turn()
            self.roll()
            self.move()
        print("Winner is " + self.turn + "!")

    def __str__(self):
        game_string = "-----------------------------------------\n"
        game_string += "Turn: " + self.turn + "\n"
        game_string += "Dice: " + str(self.dice) + "\n"
        game_string += str(self.board)
        game_string += "\n"
        return game_string


if __name__ == "__main__":
    game = Game("Black", "White")
    game.play()
