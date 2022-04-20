class Ship:
    coordinates = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
    def __init__(self, x, y, size, direct):
        self.x = Ship.coordinates[x]
        self.y = y
        self.size = size
        self.direction = direct
        self.constr_ship = self.ship_construction()

    def ship_construction(self):
        list_ship = []
        if self.direction == 'X':
            new_x = self.x + (self.size - 1)
            for i in range(self.x, new_x+1):
                list_ship.append((i, self.y))
        elif self.direction == 'Y':
            new_y = self.y + (self.size - 1)
            for i in range(self.y, new_y + 1):
                list_ship.append((self.x, i))
        else:
            raise ValueError("Некорректная переменная. Введите 'X' или 'Y'.")
        return list_ship

#    def hit_ship(self, hit_coord):
#        if hit_coord in self.constr_ship and self.size > 1:
#            self.size -= 1
#            print('Попадание в корабль!')
#        elif hit_coord in self.constr_ship and self.size == 1:
#            self.size -= 1
#            print('Убит!')
#        else:
#            print('Промах')

#    def change_coord_on_hit(self):

class Board:

    def __init__(self):
        self.ships = []

    def add_ship(self, x, y, size, direct):
        new_ship = Ship(x, y, size, direct)
        isExist = False
        for newShipCoord in new_ship.constr_ship:
            for existShip in self.ships:
                if newShipCoord in existShip.constr_ship:
                    isExist = True
                    print('Выберите другие координаты')
                    break
        if not isExist:
            self.ships.append(new_ship)

    def fire_ship(self, ship_coord_x, ship_coord_y):
        if ship_coord_x in ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J'] and len(ship_coord_x) == 1 \
                and int(ship_coord_y) in range(1, 11) and len(ship_coord_y) == 1:
            for i in self.ships:
                for j in i.constr_ship:
                    if j == (Ship.coordinates[ship_coord_x], int(ship_coord_y)):
                        i.constr_ship.remove(j)
                        print('Good job! You hit a ship!')
                if i.constr_ship == []:
                    self.ships.remove(i)
                    print('You destroyed a ship!')
        elif ship_coord_x not in ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J'] or len(ship_coord_x) != 1 \
            or len(ship_coord_y) != 1 or type(int(ship_coord_y)) != int:
            print('Input correct data!')
        else:
            print('Input correct data!')

# game_on

new_game = Board()
enough_ships = False
count_ships = 0
while not enough_ships:
    if count_ships < 2:
        new_game.add_ship(input("Input coord A-J "), int(input("Input coord 1-10 ")), int(input("Input size of the ship 1-4 ")), (input("Input X or Y ")))
        count_ships += 1
    else:
        enough_ships = True
print(new_game.ships)
print('Game on!!!')
while new_game.ships != []:
    new_game.fire_ship(input('Input coord A-J '), input("Input coord 1-10 "))
    print(new_game.ships)
print('You Won!')








