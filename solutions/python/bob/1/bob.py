def response(hey_bob):
    
    hey_bob = hey_bob.strip()
    responses = [
        'Sure.',
        'Whoa, chill out!',
        'Calm down, I know what I\'m doing!',
        'Fine. Be that way!',
        'Whatever.'
    ]

    resp_idx = None
    if len(hey_bob) > 0:
        if hey_bob[-1] == '?' and hey_bob.isupper():
            resp_idx = 2
        elif hey_bob[-1] == '?':
            resp_idx = 0
        elif hey_bob.isupper():
            resp_idx = 1
        elif hey_bob.isspace():
            resp_idx = 3
        else:
            resp_idx = 4
    else:
        resp_idx = 3

    return responses[resp_idx]