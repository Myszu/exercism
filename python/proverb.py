def proverb(*args, **kwargs):
    output = []
    end = []
    qualifier = kwargs['qualifier']
    for i, word in enumerate(args):
        if i == 0 and qualifier is None:
            end.append(f"And all for the want of a {word}.")
        elif i == 0 and qualifier is not None:
            end.append(f"And all for the want of a {qualifier} {word}.")
        else:
            output.append(f"For want of a {args[(i - 1)]} the {word} was lost.")
    return output + end
