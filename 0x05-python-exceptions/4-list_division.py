#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    tot = []

    for i in range(list_length):
        try:
            div = my_list_[i] / my_list_2[i]

        except IndexError:
            print("out of range")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except (TypeError, ValueError):
            print("wrong type")
            div = 0

        finally:
            tot.append(div)

    return tot
