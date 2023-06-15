YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: sum(i for i in dice if i == 1)
TWOS = lambda dice: sum(i for i in dice if i == 2)
THREES = lambda dice: sum(i for i in dice if i == 3)
FOURS = lambda dice: sum(i for i in dice if i == 4)
FIVES = lambda dice: sum(i for i in dice if i == 5)
SIXES = lambda dice: sum(i for i in dice if i == 6)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and any(dice.count(i) == 3 for i in set(dice)) else 0
FOUR_OF_A_KIND = lambda dice: sum(i * 4 for i in set(dice) if dice.count(i) >= 4)
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = sum


def score(dice, category):
    return category(dice)
