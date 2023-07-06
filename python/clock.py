class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        if self.minute >= 60 or self.minute < 0: self.hour += self.minute//60
        if self.hour < 0:
            self.hour = 24-(abs(self.hour)%24)
        if self.hour >=24:
            self.hour = 0 + self.hour%24     
        self.minute = self.minute%60


    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'


    def __str__(self):
        minutes = f'0{self.minute}' if self.minute < 10 else f'{self.minute}'
        hours = f'0{self.hour}' if self.hour < 10 else f'{self.hour}'
        return f'{hours}:{minutes}'


    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        return False


    def __add__(self, minutes):
        self.minute += minutes
        if self.minute >= 60 or self.minute < 0: self.hour += self.minute//60
        if self.hour >=24:
            self.hour = 0 + self.hour%24     
        self.minute = self.minute%60
        return self.__str__()


    def __sub__(self, minutes):
        self.minute -= minutes
        if self.minute >= 60 or self.minute < 0: self.hour += self.minute//60
        if self.hour < 0:
            self.hour = 24-(abs(self.hour)%24)
        if self.hour >=24:
            self.hour = 0 + self.hour%24 
        self.minute = self.minute%60
        return self.__str__()
