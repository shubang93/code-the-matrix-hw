# version code 3ebd92e7eece+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent
from vec import Vec



## 1: (Task 1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    '''

    Args:
        s:
        t:

    Returns:
    >>> a0 = list2vec([one,one,0,one,0,one])
    >>> b0 = list2vec([one,one,0,0,0,one])
    >>> v = choose_secret_vector(0,0)
    '''
    while True:
        u = list2vec([randGF2() for r in range(len(a0.D))])
        if a0*u == s and b0*u == t:
            return u



## 2: (Task 2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
def combination_util(L, n, r, index, data, i, result):
    if index==r:
        result.append(data.copy())
        return

    if i>=n:
        return

    data[index] = L[i]
    combination_util(L, n, r, index+1, data, i+1, result)
    combination_util(L, n, r, index, data, i+1, result)

def combinations(L, n, r):
    '''

    Args:
        L:
        n:
        r:

    Returns:
    >>> combinations([1,2,3,4,5], 5, 3)
    [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
    '''
    data = list([0,0,0])
    result = list()
    combination_util(L, n, r, 0, data, 0, result)
    return result

def secret_vec_list():
    '''

    Returns:
    >>> secret_vec_list()
    '''
    iter_list = combinations([0,1,2,3,4], 5, 3)
    while True:
        vec_list_a = [list2vec([randGF2() for r in range(len(a0.D))]) for r in range(4) ]
        vec_list_b = [list2vec([randGF2() for r in range(len(a0.D))]) for r in range(4) ]
        vec_list_a.append(a0)
        vec_list_b.append(b0)
        found = True
        for i in range(len(iter_list)):
            six_vec = list()
            for j in iter_list[i]:
                six_vec.append(vec_list_a[j])
                six_vec.append(vec_list_b[j])
            if not is_independent(six_vec):
                found = False
                break;
        if(found):
            print(vec_list_a)
            print(vec_list_b)
            break;
        else:
            continue
    return


secret_a0 = a0
secret_b0 = b0
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: one, 5: one})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: one, 4: 0, 5: one})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: 0, 4: one, 5: one})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: 0, 4: 0, 5: one})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: one, 4: one, 5: 0})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: 0, 4: 0, 5: one})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: 0, 4: 0, 5: one})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: 0})

