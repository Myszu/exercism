def recite(start, take=1):
    numbers = {
        10: 'Ten',
        9: 'Nine',
        8: 'Eight',
        7: 'Seven',
        6: 'Six',
        5: 'Five',
        4: 'Four',
        3: 'Three',
        2: 'Two',
        1: 'One',
        0: 'No'
    }
    output = []
    for i in range(start, start-take, -1):
        if i == 2:
            variety = ['bottles', 'bottle']
        elif i == 1:
            variety = ['bottle', 'bottles']
        else:
            variety = ['bottles', 'bottles']
        verse = [
            f"{numbers.get(i)} green {variety[0]} hanging on the wall,",
            f"{numbers.get(i)} green {variety[0]} hanging on the wall,",
            f"And if one green bottle should accidentally fall,",
            f"There'll be {(numbers.get(i-1)).lower()} green {variety[1]} hanging on the wall.",
        ]
        if i-1 > start-take and take > 1:
            verse.append("")
        output.extend(verse)
    return output
