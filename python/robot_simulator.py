# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)
    
                
    def move(self, instructions):
        self.instructions = instructions

        for letter in self.instructions:
            if letter == 'L':
                self.turn_left()
                continue
            
            if letter == 'R':
                self.turn_right()
                continue
            
            if letter == 'A':
                self.advance()
                continue
                
                
    def turn_left(self):
        match self.direction:
            case 0:
                self.direction = NORTH
            case 1:
                self.direction = WEST
            case 2:
                self.direction = SOUTH
            case 3:
                self.direction = EAST


    def turn_right(self):
        match self.direction:
            case 0:
                self.direction = SOUTH
            case 1:
                self.direction = EAST
            case 2:
                self.direction = NORTH
            case 3:
                self.direction = WEST


    def advance(self):
        match self.direction:
            case 0:
                self.x_pos += 1
            case 1:
                self.y_pos += 1
            case 2:
                self.x_pos -= 1
            case 3:
                self.y_pos -= 1
        self.coordinates = (self.x_pos, self.y_pos)
