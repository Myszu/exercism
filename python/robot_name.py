import random
from random import randint

class Robot:
    def __init__(self):
        self.letters = 2
        self.digits = 3
        self.name = self.generate()
        
        
    def generate(self) -> str:
        output = ''
        ABC = 'ABCDEFGIJKLMNOPQRSTUVWXYZ'
        for i in range(self.letters):
            random.seed(None)
            output += ABC[randint(0, len(ABC)-1)]
        for i in range(self.digits):
            random.seed(None)
            output += str(randint(0, 9))
        return output

        
    def reset(self):
        self.name = self.generate()
