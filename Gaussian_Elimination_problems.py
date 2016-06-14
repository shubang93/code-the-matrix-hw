# version code 021f9affec63+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one


def convert_to_echelon(M):
    '''
    Input:
        - M: a Matrix
    Output:
        - A: a Matrix converted to echelon form
    Examples:
        >>> convert_to_echelon(identity(range(4), 1)) == identity(range(4), 1)
        True
    '''
    row_list = list(mat2rowdict(M).values())
    col_label_list = sorted(row_list[0].D, key=hash)
    rows_left = set(range(len(row_list)))
    new_row_list = list()
    for c in col_label_list:
        rows_non_zero = [r for r in rows_left if row_list[r][c] !=0 ]
        if rows_non_zero != []:
            pivot_row = rows_non_zero[0]
            new_row_list.append(row_list[pivot_row])
            rows_left.remove(pivot_row)
            for r in rows_non_zero[1:]:
                multiplier = row_list[r][c]/row_list[pivot_row][c]
                row_list[r] -= multiplier*row_list[pivot_row]
    return rowdict2mat(new_row_list)







## 1: (Problem 1) Recognizing Echelon Form
# Write each matrix as a list of row lists

echelon_form_1 = [[   1, 2, 0, 2, 0   ],
                  [   0, 1, 0, 3, 4   ],
                  [   0, 0, 2, 3, 4   ],
                  [   0, 0, 0, 2, 0   ],
                  [   0, 0, 0, 0, 4   ]]

echelon_form_2 = [[   0, 4, 3, 4, 4   ],
                  [   0, 0, 4, 2, 0   ],
                  [   0, 0, 0, 0, 1   ],
                  [   0, 0, 0, 0, 0   ]]

echelon_form_3 = [[   1, 0, 0, 1   ],
                  [   0, 0, 0, 1   ],
                  [   0, 0, 0, 0   ]]

echelon_form_4 = [[   1, 0, 0, 0   ],
                  [   0, 1, 0, 0   ],
                  [   0, 0, 0, 0   ],
                  [   0, 0, 0, 0   ]]



## 2: (Problem 2) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[9,-1,2],[0,4,5],[0,0,2]])
        True
        >>> is_echelon([[0,4,5],[0,3,0],[0,0,2]])
        False
        >>> is_echelon([[9,10]])
        True
        >>> is_echelon([[5]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
        >>> is_echelon([[1,0,2],[0,0,0],[0,0,-1]])
        False
        >>> is_echelon([[7,1,0],[0,5,0],[0,0,0],[0,0,0]])
        True
    '''
    row_range = list(reversed(range(len(A))))
    row_range.remove(0)
    col_range = range(len(A[0]))
    for r in row_range:
        k = len(col_range)
        k_1 = len(col_range)-1
        row = A[r]
        row_1 = A[r-1]
        for c in col_range:
            if row[c] !=0:
                k = c
                break
        for c in col_range:
            if row_1[c] !=0:
                k_1 = c
                break
        if k_1 >= k:
            return False
    return True





## 3: (Problem 3) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## 4: (Problem 4) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21, 0, 2, 0, 0]



## 5: (Problem 5) Echelon Solver
def echelon_solve(row_list, label_list, b):
    '''
    Input:
        - row_list: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in row_list
        - b: a vector (represented as a list)
    Output:
        - Vec x such that row_list * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    >>> U_rows == [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    True
    >>> b_list == [one,0,one]
    True
    '''
    pass



## 6: (Problem 6) Solving General Matrices via Echelon
row_list = [ ... ]    # Provide as a list of Vec instances
label_list = [ ... ] # Provide as a list
b = [ ... ]          # Provide as a list of GF(2) values



## 7: (Problem 7) Nullspace A
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## 8: (Problem 8) Nullspace B
null_space_rows_b = {...} # Put the row numbers of M from the PDF

