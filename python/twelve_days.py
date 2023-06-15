def recite(start_verse, end_verse):
    gifts = [
        'a Partridge in a Pear Tree.',
        'two Turtle Doves',
        'three French Hens',
        'four Calling Birds',
        'five Gold Rings',
        'six Geese-a-Laying',
        'seven Swans-a-Swimming',
        'eight Maids-a-Milking',
        'nine Ladies Dancing',
        'ten Lords-a-Leaping',
        'eleven Pipers Piping',
        'twelve Drummers Drumming'
    ]
    day_strings = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    output = []
    for i in range(start_verse, end_verse + 1):
        verse = (f'On the {day_strings[i-1]} day of Christmas my true love gave to me: ')
        for j in range(i, 0, -1):
            if i > 1 and j == 1:
                verse += (', and ' + gifts[j - 1])
                break
            elif j != i:
                verse += (', ' + gifts[j - 1])
                continue
            verse += (gifts[j - 1])
        output.append(verse)
    return output
