from src.Point import Point


class Board:

    def __init__(self, checker_color1, checker_color2):
        self.checker_color1 = checker_color1
        self.checker_color2 = checker_color2
        self.points = [Point(None, 0)] * 24
        self.points[23] = Point(checker_color1, 2)
        self.points[18] = Point(checker_color2, 5)
        self.points[16] = Point(checker_color2, 3)
        self.points[12] = Point(checker_color1, 5)
        self.points[11] = Point(checker_color2, 5)
        self.points[7] = Point(checker_color1, 3)
        self.points[5] = Point(checker_color1, 5)
        self.points[0] = Point(checker_color2, 2)
        self.bar = {checker_color1: 0, checker_color2: 0}
        self.total_off = {checker_color1: 0, checker_color2: 0}

    def __str__(self):
        # fill this in next time
        return

    def _hit_or_add_checker(self, checker_color, point):
        if self.points[point].can_hit(checker_color):
            self.points[point].hit(checker_color)
            if checker_color == self.checker_color1:
                self.bar[self.checker_color2] += 1
            else:
                self.bar[self.checker_color1] += 1
        else:
            assert self.points[point].can_add_checker(checker_color)
            self.points[point].add_checker(checker_color)

    def has_checkers_on_bar(self, checker_color):
        assert(checker_color == self.checker_color1 or checker_color == self.checker_color2)
        return self.bar[checker_color] > 0

    def has_all_checkers_home(self, checker_color):
        assert (checker_color == self.checker_color1 or checker_color == self.checker_color2)
        total_checkers_home = 0
        home_point = 0
        if checker_color == self.checker_color2:
            home_point = 18
        for point in range(home_point, home_point + 6):
            if self.points[point].checker_color == checker_color:
                total_checkers_home += self.points[point].checker_count
        total_checkers_home += self.total_off[checker_color]
        return not (total_checkers_home != 15)

    def is_winner(self, checker_color):
        assert (checker_color == self.checker_color1 or checker_color == self.checker_color2)
        return self.total_off[checker_color] == 15

    def can_take_off_bar(self, checker_color, point):
        assert(checker_color == self.checker_color1 or checker_color == self.checker_color2)
        assert(0 < point < 7)
        if checker_color == self.checker_color1:
            point = 24 - point
        else:
            point -= 1
        if not self.points[point].can_hit(checker_color) and not self.points[point].can_add_checker(checker_color):
            return False
        if not self.has_checkers_on_bar(checker_color):
            return False
        return True

    def take_off_bar(self, checker_color, point):
        if not self.can_take_off_bar(checker_color, point):
            raise RuntimeError("Cannot take checker off of the bar")
        self.bar[checker_color] -= 1
        if checker_color == self.checker_color1:
            point = 24 - point
        else:
            point -= 1
        self._hit_or_add_checker(checker_color, point)

    def can_move(self, checker_color, point, spaces):
        assert(checker_color == self.checker_color1 or checker_color == self.checker_color2)
        assert(0 <= point < 24)
        assert(0 < spaces < 7)
        if checker_color == self.checker_color1:
            spaces *= -1
        point_ahead = point + spaces
        if point_ahead < 0 or point_ahead > 23:
            return False
        if self.has_checkers_on_bar(checker_color):
            return False
        if not self.points[point].can_remove_checker(checker_color):
            return False
        if not self.points[point_ahead].can_hit(checker_color) and not self.points[point_ahead].can_add_checker(checker_color):
            return False
        return True

    def move(self, checker_color, point, spaces):
        if not self.can_move(checker_color, point, spaces):
            raise RuntimeError("Cannot move checker piece")
        if checker_color == self.checker_color1:
            spaces *= -1
        point_ahead = point + spaces
        self.points[point].remove_checker(checker_color)
        self._hit_or_add_checker(checker_color, point_ahead)

    def can_bear_off(self, checker_color, point, spaces):
        assert (checker_color == self.checker_color1 or checker_color == self.checker_color2)
        assert (0 <= point < 24)
        assert (0 < spaces < 7)
        if checker_color == self.checker_color1:
            spaces *= -1
        point_ahead = point + spaces
        if point_ahead >= 0 or point_ahead < 24:
            return False
        if not self.has_all_checkers_home(checker_color):
            return False
        if self.can_move(checker_color, point, spaces):
            return False
        if not self.points[point].can_remove_checker(checker_color):
            return False
        return True

    def bear_off(self, checker_color, point, spaces):
        if not self.can_bear_off(checker_color, point, spaces):
            raise RuntimeError("Cannot bear off checker")
        self.points[point].remove_checker(checker_color)
        self.total_off[checker_color] += 1
