class NORTH:

    def __init__(self):
        self.direction = getattr(NORTH, 'NORTH')


class EAST:

    def __init__(self):
        self.direction = getattr(EAST, 'EAST')


class SOUTH:

    def __init__(self):
        self.direction = getattr(SOUTH, 'SOUTH')


class WEST:

    def __init__(self):
        self.direction = getattr(WEST, 'WEST')


class Robot(NORTH, SOUTH, EAST, WEST):

    def __init__(self, bearing=NORTH, x_coordinate=0, y_coordinate=0):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.bearing = bearing
        self.coordinates = (x_coordinate, y_coordinate)

    def simulate(self, instruction_string):
        self.coordinates = list(self.coordinates)
        for letter in instruction_string.lower():
            if letter == 'a':
                self.advance()
            elif letter == 'r':
                self.turn_right()
            elif letter == 'l':
                self.turn_left()
        self.coordinates = tuple(self.coordinates)

    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        else:
            self.bearing = NORTH

    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        else:
            self.bearing = NORTH


    def advance(self):
        self.coordinates = list(self.coordinates)
        if self.bearing == NORTH:
            self.coordinates[1] += 1
        elif self.bearing == SOUTH:
            self.coordinates[1] -= 1
        elif self.bearing == EAST:
            self.coordinates[0] += 1
        else:
            self.coordinates[0] -= 1
        self.coordinates = tuple(self.coordinates)