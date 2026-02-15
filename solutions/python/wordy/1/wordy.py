OPERATIONS = {
    "plus": lambda a, b: a + b,
    "minus": lambda a, b: a - b,
    "multiplied by": lambda a, b: a * b,
    "divided by": lambda a, b: a / b
}

def answer(question):
    words = question[:-1].strip().replace("What is ", "").split()
    if len(words) == 0:
        raise ValueError("syntax error")
    
    op = []
    expect_num = True
    iter = 0
    while iter < len(words):
        if expect_num:
            try:
                op.append(int(words[iter]))
            except:
                raise ValueError("syntax error")
            
            expect_num = False
            
        else:
            try:            
                int(words[iter])
            except ValueError:            
                if iter + 1 < len(words) and f"{words[iter]} {words[iter+1]}" in OPERATIONS:
                    op_word = f"{words[iter]} {words[iter+1]}"
                    iter += 1
                elif words[iter] in OPERATIONS:
                    op_word = words[iter]
                else:
                    raise ValueError("unknown operation")
                
                op.append(OPERATIONS.get(op_word))
                expect_num = True
            else:        
                raise ValueError("syntax error")

        iter += 1
    
    if not isinstance(op[-1], int):
        raise ValueError("syntax error")
        
    total = op[0]
    for func, rhs in zip(op[1::2], op[2::2]):
        total = func(total, rhs)
    return total