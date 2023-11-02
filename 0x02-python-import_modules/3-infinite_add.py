#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    larg = len(sys.argv)
    summ = 0;

    if larg == 1:
        print(0)
    for i in range(1, larg):
        summ = summ + int(sys.argv[i])
    print(summ)
