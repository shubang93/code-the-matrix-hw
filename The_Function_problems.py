# version code 542eddf1f327+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> tuple_sum([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''
    # ret = []
    # for i in range(len(A)):
    #     a = A[i]
    #     b = B[i]
    #     ret.append((a[0]+b[0], a[1]+b[1]))
    #return ret
    return [(A[i][0]+B[i][0], A[i][1]+B[i][1]) for i in range(len(A))]

print("Tuple sum: ", tuple_sum([(1,2), (10,20)],[(3,4), (30,40)]))
print("Tuple sum: ", tuple_sum([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)]))

## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''

    return {value:key for key, value in d.items()}

print("Inv_Dict: ", inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}))

## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [p+i for i in range(n)]

print("Row test: ", row(10,4))

comprehension_with_row = [row(p, 20) for p in range(15)]

print("Comp with row: ", comprehension_with_row)

comprehension_without_row = [[p+i for i in range(20)] for p in range(15)]
print("Comp without row: ", comprehension_without_row)


## 4: (Problem 4) Probability Exercise 1
f = {1, 2, 3, 5, 6}
funct = {key:key+1 for key in f}
prob = {1:0.5, 2:0.2, 3:0.1, 5:0.1, 6:0.1}
Pr_f_is_even = 0.0
Pr_f_is_odd  = 0.0
for key in funct.keys():
    if funct[key]%2==0:
        Pr_f_is_even = Pr_f_is_even+prob[key]
    else:
        Pr_f_is_odd = Pr_f_is_odd+prob[key]

print("Even probabillty: ", Pr_f_is_even)
print("Odd probability:", Pr_f_is_odd)


## 5: (Problem 5) Probability Exercise 2
Pr_g_is_1    = 0.0
Pr_g_is_0or2 = 0.0
g_domain = {1, 2, 3, 4, 5, 6, 7}
g = {key:key%3 for key in g_domain}
g_prob = {1:0.2, 2:0.2, 3:0.2, 4:0.1, 5:0.1, 6:0.1, 7:0.1}
for key in g.keys():
    if g[key]%3==1:
        Pr_g_is_1 = Pr_g_is_1 + g_prob[key]
    else:
        Pr_g_is_0or2 = Pr_g_is_0or2 + g_prob[key]


print("Prob for remainder of 1: ", Pr_g_is_1)
print("Prob for remainder of 0 or 2: ", Pr_g_is_0or2)
