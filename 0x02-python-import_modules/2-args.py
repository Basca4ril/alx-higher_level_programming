#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    larg = len(sys.argv)

    if (larg == 1):
        print("{} arguments.".format(larg - 1))
    elif (larg > 1):
        if (larg == 2):
            print("{} argument:".format(larg - 1))
            print("{}: {}".format(larg - 1, sys.argv[larg-1]))
        else:
            print("{} arguments:".format(larg - 1))
            for i in range(1, larg):
                print("{}: {}".format(i, sys.argv[i]))
