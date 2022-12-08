#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
       A function that returns thequare value of all elements in a 
       multi dimensional list being passsed as arguments.

       Alllowed to use regular loops, map, etc
    '''
    new_1st = []
    if len(matrix) == 0:
        return new_1st

    new_1st = [[i*i for i in j] for j in matrix]
    return new_1st
