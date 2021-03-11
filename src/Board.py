from src.Point import Point


class Board:

    def __init__(self, checker_color1, checker_color2):
        self.points = [Point(None, 0)] * 24
        self.points[23] = Point(checker_color1, 2)
        self.points[18] = Point(checker_color2, 5)
        self.points[16] = Point(checker_color2, 3)
        self.points[12] = Point(checker_color1, 5)
        self.points[11] = Point(checker_color2, 5)
        self.points[7] = Point(checker_color1, 3)
        self.points[5] = Point(checker_color1, 5)
        self.points[0] = Point(checker_color2, 2)


if __name__ == "__main__":
    Board("black", "white")

