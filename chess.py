class Piece:
    __slots__ = ('x', 'y')
    coordinates = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    """ Класс фигура"""
    def __init__(self, source_coordinate):
        """ Входные данные координат фигуры """
        self.x = Piece.coordinates[source_coordinate[0]]
        self.y = int(source_coordinate[1])

    @staticmethod
    def convert_coord_to_nums(coord):
        x = Piece.coordinates[coord[0]]
        y = int(coord[1])
        return x, y

    def next_step(self, new_source_coordinate):
        """ Метод реализующий шаг фигуры """
        new_x, new_y = self.convert_coord_to_nums(new_source_coordinate)

    @staticmethod
    def can_move(new_x, new_y):
        """ Метод, проверяющий корректность шага """
        if not new_x >= 1 and new_x <= 8 and new_y >= 1 and new_y <= 8:
            raise BadStep

    def get_coord(self):
        return str(list(Piece.coordinates.keys())[list(Piece.coordinates.values()).index(self.x)]) + str(self.y)


class Pawn(Piece):
    """ Класс для пешки """
    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)
    def next_step(self, new_source_coordinate):
        """ Метод, проверяющий корректность шага пешки """
        if new_source_coordinate[0] in ["A", "B", "C", "D", "E", "F", "G", "H"] \
                and int(new_source_coordinate[1]) in range(1, 9) and len(new_source_coordinate) == 2:
            new_x, new_y = self.convert_coord_to_nums(new_source_coordinate)
            if not super().can_move(new_x, new_y):
                if self.x == new_x and new_y == self.y + 1 or (new_y == self.y + 2 and  self.y == 2):
                    self.x = new_x
                    self.y = new_y
                else:
                    raise BadStep
        else:
            raise WrongArgument

class King(Piece):
    """ Класс для короля """
    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)
    def next_step(self, new_source_coordinate):
        """ Метод, проверяющий корректность шага короля """
        if new_source_coordinate[0] in ["A", "B", "C", "D", "E", "F", "G", "H"] \
                and int(new_source_coordinate[1]) in range(1,9) and len(new_source_coordinate) == 2:
            new_x, new_y = self.convert_coord_to_nums(new_source_coordinate)
            if not super().can_move(new_x, new_y):
                if abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1:
                    self.x = new_x
                    self.y = new_y
                else:
                    raise BadStep
        else:
            raise WrongArgument

class Rook(Piece):
    """ Класс для ладьи """
    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)
    def next_step(self, new_source_coordinate):
        """ Метод, проверяющий корректность шага ладьи """
        if new_source_coordinate[0] in ["A", "B", "C", "D", "E", "F", "G", "H"] \
                and int(new_source_coordinate[1]) in range(1, 9) and len(new_source_coordinate) == 2:
            new_x, new_y = self.convert_coord_to_nums(new_source_coordinate)
            if not super().can_move(new_x, new_y):
                if (new_x == self.x and (new_y < self.y or new_y > self.y)) \
                        or (new_y == self.y and (new_x < self.x or new_x > self.x)):
                    self.x = new_x
                    self.y = new_y
                else:
                    raise BadStep
        else:
            raise WrongArgument

class Bishop(Piece):
    """ Класс для слона """
    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)

    def next_step(self, new_source_coordinate):
        """ Метод, проверяющий корректность шага слона """
        if new_source_coordinate[0] in ["A", "B", "C", "D", "E", "F", "G", "H"] \
                and int(new_source_coordinate[1]) in range(1, 9) and len(new_source_coordinate) == 2:
            new_x, new_y = self.convert_coord_to_nums(new_source_coordinate)
            if not super().can_move(new_x, new_y):
                if abs(new_x - self.x) == abs(new_y - self.y):
                    self.x = new_x
                    self.y = new_y
                else:
                    raise BadStep
        else:
            raise WrongArgument

class Knight(Piece):
    """ Класс для коня """
    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)
    def next_step(self, new_source_coordinate):
        """ Метод, проверяющий корректность шага коня """
        if new_source_coordinate[0] in ["A", "B", "C", "D", "E", "F", "G", "H"] \
                and int(new_source_coordinate[1]) in range(1, 9) and len(new_source_coordinate) == 2:
            new_x, new_y = self.convert_coord_to_nums(new_source_coordinate)
            if not super().can_move(new_x, new_y):
                if (abs(new_x - self.x) == 1 and abs(new_y - self.y) == 2) \
                        or (abs(new_x - self.x) == 2 and abs(new_y - self.y) == 1):
                    self.x = new_x
                    self.y = new_y
                else:
                    raise BadStep
        else:
            raise WrongArgument

class Queen(Piece):
    """ Класс для королевы """
    def __init__(self, source_coordinate):
        super().__init__(source_coordinate)
    def next_step(self, new_source_coordinate):
        """ Метод, проверяющий корректность шага королевы """
        if new_source_coordinate[0]  in ["A", "B", "C", "D", "E", "F", "G", "H"] \
                and int(new_source_coordinate[1]) in range(1, 9) and len(new_source_coordinate) == 2:
            new_x, new_y = self.convert_coord_to_nums(new_source_coordinate)
            if not super().can_move(new_x, new_y):
                if (abs(new_x - self.x) == abs(new_y - self.y)) \
                    or (new_x == self.x and (new_y < self.y or new_y > self.y)) \
                    or (new_y == self.y and (new_x < self.x or new_x > self.x)):
                    self.x = new_x
                    self.y = new_y
                else:
                    raise BadStep
        else:
            raise WrongArgument

def get_figure(name,source):
    if source[0] in ["A", "B", "C", "D", "E", "F", "G", "H"] \
            and int(source[1]) in range(1,9) and len(source) == 2:
        if name == 'rook':
            return Rook(source)
        elif name == 'knight':
            return Knight(source)
        elif name == 'bishop':
            return Bishop(source)
        elif name == 'pawn':
            return Pawn(source)
        elif name == 'king':
            return King(source)
        elif name == 'queen':
            return Queen(source)
    else:
        raise WrongArgument


class BadStep(Exception):
    pass

class WrongArgument(Exception):
    pass