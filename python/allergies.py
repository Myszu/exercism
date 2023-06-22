class Allergies(object):
    def __init__(self, score):
        self.score = score
        self.allergens = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128}
        self._lst = [allergen for (allergen, score) in self.allergens.items() if self.score & score != 0]

        
    def allergic_to(self, item):
        return item in self._lst

        
    @property
    def lst(self):
        return self._lst
