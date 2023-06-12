def recite(start_verse, end_verse):
    verses = {
            'that lay in ': 'the house that Jack built.',
            'that ate ': 'the malt',
            'that killed ': 'the rat',
            'that worried ': 'the cat',
            'that tossed ': 'the dog',
            'that milked ': 'the cow with the crumpled horn',
            'that kissed ': 'the maiden all forlorn',
            'that married ': 'the man all tattered and torn',
            'that woke ': 'the priest all shaven and shorn',
            'that kept ': 'the rooster that crowed in the morn',
            'that belonged to ': 'the farmer sowing his corn',
            '': 'the horse and the hound and the horn'
    }
    
    prefix = list(verses.keys())
    output = []
    
    for i in range(start_verse -1, end_verse):
        single = 'This is '
        for j in range(end_verse):
            if j == 0:
                single += verses[prefix[end_verse - j - 1]]
            else:
                single += ' ' + prefix[end_verse - j - 1] + verses[prefix[end_verse - j - 1]]
        output.insert(0, single)
        end_verse -= 1
    return output
