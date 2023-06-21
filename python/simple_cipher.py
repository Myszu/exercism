from secrets import randbelow
class Cipher:
    def __init__(self, key: str =None):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if not key:
            self.key = self.gen_key()
        else:
            self.key = key.lower()


    def encode(self, text):
        output =''
        if len(text) > len(self.key):
            self.key += self.key*(len(text) // len(self.key))
        for i, letter in enumerate(text):
            shift = self.alphabet.index(letter) + self.alphabet.index(self.key[i])
            if shift >= 26: shift -= 26
            output += ''.join(self.alphabet[shift])
        return output


    def decode(self, text):
        output =''
        if len(text) > len(self.key):
            self.key += self.key*(len(text) // len(self.key))
        for i, letter in enumerate(text):
            shift = 26 - (self.alphabet.index(self.key[i]) - self.alphabet.index(letter))
            if shift >= 26: shift -= 26
            output += ''.join(self.alphabet[shift])
        return output
    
    
    def gen_key(self):
        output = ''
        for i in range(100):
            output += ''.join(self.alphabet[randbelow(26)])
        return output
