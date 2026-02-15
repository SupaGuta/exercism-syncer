OPERATIONS = {
    "plus": lambda a, b: a + b,
    "minus": lambda a, b: a - b,
    "multiplied": lambda a, b: a * b,
    "divided": lambda a, b: a / b
}

def answer(question):
    words = question.removeprefix("What is").removesuffix("?").replace("by", "").strip().split()
    if len(words) == 0:
        raise ValueError("syntax error")
    
    equation = []
    expect_num = True
    iter = 0
    while iter < len(words):
        if expect_num:
            try:
                equation.append(int(words[iter]))
            except:
                raise ValueError("syntax error")
            
            expect_num = False
            
        else:
            try:            
                int(words[iter])
            except ValueError:            
                if words[iter] in OPERATIONS:
                    op_word = words[iter]
                else:
                    raise ValueError("unknown operation")
                
                equation.append(OPERATIONS.get(op_word))
                expect_num = True
            else:        
                raise ValueError("syntax error")

        iter += 1
    
    if not isinstance(equation[-1], int):
        raise ValueError("syntax error")
        
    total = equation[0]
    for operation, next_number in zip(equation[1::2], equation[2::2]):
        total = operation(total, next_number)
    return total