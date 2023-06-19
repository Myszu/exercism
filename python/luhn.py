import re
class Luhn:
    def __init__(self, card_num:str):
        self.card_num = card_num.replace(' ', '')


    def valid(self):
        if re.findall('[a-zA-Z!@#$%^&*(),.]', self.card_num):
            return False
        if len(self.card_num) < 2:
            return False
        buffer = []
        for i, digit in enumerate(self.card_num[::-1]):
            if not digit.isnumeric():
                continue
            if (i + 1)%2 == 0:
                double = int(digit)*2
                if not double > 9:
                    buffer.append(double)
                    continue
                buffer.append(double-9)
                continue
            buffer.append(int(digit))
        if sum(buffer)%10 == 0:
            return True
        return False
