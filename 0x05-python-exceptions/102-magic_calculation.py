#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    try:
        for i in range(1, 3):
            result += (a ** b) / i
    except Exception as e:
        if e.args[0] == 'Too far':
            raise
        else:
            raise Exception('Unexpected exception')

    else:
        result += b + a

    return result
