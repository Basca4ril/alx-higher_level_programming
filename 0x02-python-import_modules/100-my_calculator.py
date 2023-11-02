#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    larg = len(sys.argv)


    if larg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]

    mull = mul(a, b)

    if c == '+':
        print("{} {} {} = {}".format(a, c, b, add(a, b)))

    elif c == '-':
        print("{} {} {} = {}".format(a, c, b, sub(a, b)))

    elif c == "*":
        print("{} {} {} = {}".format(a, c, b, mul(a, b)))

    elif c == '/':
        print("{} {} {} = {}".format(a, c, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
