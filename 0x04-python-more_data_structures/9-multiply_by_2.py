#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dic = a_dictionary.copy()
    for k in n_dic:
        n_dic[k] *= 2
    return (n_dic)
