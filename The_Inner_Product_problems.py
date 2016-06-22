# version code 3ebd92e7eece+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from vecutil import list2vec



## 1: (Problem 1) Norm
norm1 = 3
norm2 = 4
norm3 = 3



## 2: (Problem 2) Closest Vector
# Write each vector as a list
def project_along(b, a):
    '''

    Args:
        b:
        a:

    Returns:
    >>> b = list2vec([1.414, 1, 1.732])
    >>> a = list2vec([0,1,0])
    >>> project_along(b, a)
    >>> b = list2vec([2, 3])
    >>> a = list2vec([1, 2])
    >>> project_along(b, a)
    >>> b = list2vec([7,2,5,0])
    >>> a = list2vec([-3,-2,-1,4])
    >>> list(project_along(b, a).f.values())
    '''
    return (((b*a)/(a*a)) if a*a > 1e-20 else 0)*a

def project_orthogonal(b, a):
    '''

    Args:
        b:
        a:

    Returns:

    '''
    return b-project_along(b, a)
closest_vector_1 = [8/5, 16/5]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## 3: (Problem 3) Projection Orthogonal to and onto Vectors
# Write each vector as a list
# round up to 6 decimal points if necessary
a1 = list2vec([3, 0])
b1 = list2vec([2, 1])
a2 = list2vec([1, 2, -1])
b2 = list2vec([1, 1, 4])
a3 = list2vec([3, 3, 12])
b3 = list2vec([1, 1, 4])
project_onto_1 = list(project_along(b1, a1).f.values())
projection_orthogonal_1 = list(project_orthogonal(b1, a1).f.values())

project_onto_2 = list(project_along(b2, a2).f.values())
projection_orthogonal_2 = list(project_orthogonal(b2, a2).f.values())

project_onto_3 = list(project_along(b3, a3).f.values())
projection_orthogonal_3 = list(project_orthogonal(b3, a3).f.values())

