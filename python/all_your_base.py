def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if any(d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if any(d < 0 for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    input = sum([digit * (input_base**i) for i, digit in enumerate(digits[::-1])])
    if input == 0: return [0]
    output = []
    
    while input != 0:
        output.append(input%output_base)
        input = input//output_base
    
    return output[::-1]