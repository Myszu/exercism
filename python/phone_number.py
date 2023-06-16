import re
class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean(number)
        self.area_code = self.number[:3]
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")

        if self.number[3] == '0':
            raise ValueError("exchange code cannot start with zero")

        if self.number[3] == '1':
            raise ValueError("exchange code cannot start with one")
        
        if self.number[0] == '0':
            raise ValueError("area code cannot start with zero")

        if self.number[0] == '1':
            raise ValueError("area code cannot start with one")
            
        if re.findall('[a-zA-Z]', self.number):
            raise ValueError("letters not permitted")
            
        if re.findall('[!@#$%^&*,]', self.number):
            raise ValueError("punctuations not permitted")
            
            
    def clean(self, input):
        cleaned = re.sub('[ ()-.]', '', input)
        if len(cleaned) == 11 and cleaned[0] != '1':
            raise ValueError("11 digits must start with 1")
            
        if len(cleaned) == 11:
            return cleaned[1:]
            
        return cleaned
    
    def pretty(self):
        return f'({self.area_code})-{self.number[3:6]}-{self.number[6:]}'
