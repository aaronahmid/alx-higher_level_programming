#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m_copy = [[(i[n]**2) for n in range(3)] for i in matrix]
    return m_copy