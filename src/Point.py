class Point:

    def __init__(self, checker_color, checker_count):
        self.checker_color = checker_color
        self.checker_count = checker_count

    def can_add_checker(self, checker_color):
        if self.checker_color is None or self.checker_color == checker_color:
            return True
        return False

    def can_remove_checker(self, checker_color):
        if self.checker_count == 0 or self.checker_color is None or self.checker_color != checker_color:
            return False
        return True

    def can_hit(self, checker_color):
        if self.checker_count == 1 and self.checker_color is not None and self.checker_color != checker_color:
            return True
        return False

    def hit(self, checker_color):
        if not self.can_hit(checker_color):
            raise RuntimeError("Point cannot be hit")
        self.checker_color = checker_color

    def add_checker(self, checker_color):
        if not self.can_add_checker(checker_color):
            raise RuntimeError("Checker cannot be added to point")
        if self.checker_count == 0:
            self.checker_color = checker_color
        self.checker_count += 1

    def remove_checker(self, checker_color):
        if not self.can_remove_checker(checker_color):
            raise RuntimeError("Checker cannot be removed from point")
        self.checker_count -= 1
        if self.checker_count == 0:
            self.checker_color = None
