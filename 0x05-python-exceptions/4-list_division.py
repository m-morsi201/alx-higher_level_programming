#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    dev_list = []
    for i in range(list_length):
        try:
            dev = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            dev = 0
        except TypeError:
            print("wrong type")
            dev = 0
        except IndexError:
            print("out of range")
            dev = 0
        finally:
            dev_list.append(dev)
    return (dev_list)
