from src.Board import Board
import random


class Game:

    def __init__(self, checker_color1, checker_color2):
        self.board = Board(checker_color1, checker_color2)
        self.player1 = checker_color1
        self.player2 = checker_color2
        self.turn = self.player1
        self.dice = (0, 0)

    def first_roll(self):
        input("Press Enter to determine initial roll ...")
        checker_color1_roll = 0
        checker_color2_roll = 0
        while checker_color1_roll == checker_color2_roll:
            checker_color1_roll = random.randint(1, 6)
            checker_color2_roll = random.randint(1, 6)
        self.dice = (checker_color1_roll, checker_color2_roll)
        if checker_color2_roll > checker_color1_roll:
            self.turn = self.player2

    def roll(self):
        self.dice = random.randint(1, 6), random.randint(1, 6)

    def play(self):
        while not self.board.is_winner(self.turn):
            input("Press enter to roll ...")
            self.roll()
            print(self)
            input("Enter the point number, followed by the roll number")

    def __str__(self):
        print("Turn: " + self.turn)
        print("Dice: " + str(self.dice[0]) + ", " + str(self.dice[1]))
        print(self.board)


if __name__ == "__main__":
    game = Game("black", "white")
    game.first_roll()
    game.play()
