def score(word):
    one = 'aeioulnrst'
    two = 'dg'
    three = 'bcmp'
    four = 'fhvwy'
    five = 'k'
    eight = 'jx'
    ten = 'qz'
    
    test_unit = {
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        eight: 8,
        ten: 10
    }
    
    score = 0
    
    for letter in word:
        for unit, point in test_unit.items():
            if letter.lower() in unit:
                score += point
                break
    return score
