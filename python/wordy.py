import re
operators = {
    "plus": "__add__",
    "minus": "__sub__",
    "multiplied by": "__mul__",
    "divided by": "__truediv__"
}

def clean_up(phrase):
    return phrase.removeprefix("What is").removesuffix("?").strip()
          

def answer(question):
    question = clean_up(question)
    if not question:
        raise ValueError("syntax error")
    if re.search(re.compile("^-?\d$"), question):
        return int(question)
    is_math = False
    for word, operator in operators.items():
        if word in question:
            question = question.replace(word, operator)
            is_math = True
    if not is_math:
        raise ValueError("unknown operation")
    calculation = question.split()
    while len(calculation) > 1:
        try:
            val_1, operator, val_2, *rest = calculation
            if operator not in operators.values():
                raise ValueError("syntax error")
            calculation = [int(val_1).__getattribute__(operator)(int(val_2)), *rest]
        except:
            raise ValueError("syntax error")
    return calculation[0]
