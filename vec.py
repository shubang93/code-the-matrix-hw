# version code 24ea27739109+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Copyright 2013 Philip N. Klein

def test_format(obj, precision=2):
    tf = lambda o: test_format(o, precision)
    delimit = lambda o: ', '.join(o)
    otype = type(obj)
    if otype is str:
        return repr(obj)
    elif otype is float or otype is int:
        if otype is int:
            obj = float(obj)
        if -0.000001 < obj < 0.000001:
            obj = 0.0
        fstr = '%%.%df' % precision
        return fstr % obj
    elif otype is set:
        if len(obj) == 0:
            return 'set()'
        return '{%s}' % delimit(sorted(map(tf, obj)))
    elif otype is dict:
        return '{%s}' % delimit(sorted(tf(k)+': '+tf(v) for k,v in obj.items()))
    elif otype is list:
        return '[%s]' % delimit(map(tf, obj))
    elif otype is tuple:
        return '(%s%s)' % (delimit(map(tf, obj)), ',' if len(obj) == 1 else '')
    elif otype.__name__ in ['Vec','Mat']:
        entries = tf({x:obj.f[x] for x in obj.f if tf(obj.f[x]) != tf(0)})
        return '%s(%s, %s)' % (otype.__name__, tf(obj.D), entries)
    else:
        return str(obj)

def getitem(v,k):
    """
    Return the value of entry k in v.
    Be sure getitem(v,k) returns 0 if k is not represented in v.f.

    >>> v = Vec({'a','b','c', 'd'},{'a':2,'c':1,'d':3})
    >>> v['d']
    3
    >>> v['b']
    0
    """
    return v.f[k] if k in v.f.keys() else 0

def setitem(v,k,val):
    """
    Set the element of v with label d to be val.
    setitem(v,d,val) should set the value for key d even if d
    is not previously represented in v.f.

    >>> v = Vec({'a', 'b', 'c'}, {'b':0})
    >>> v['b'] = 5
    >>> v['b']
    5
    >>> v['a'] = 1
    >>> v['a']
    1
    >>> v['a'] = 0
    >>> v['a']
    0
    """
    assert k in v.D
    v.f[k] = val
    return

def equal(u,v):
    """
    Return true iff u is equal to v.
    Because of sparse representation, it is not enough to compare dictionaries

    >>> Vec({'a', 'b', 'c'}, {'a':0}) == Vec({'a', 'b', 'c'}, {'b':0})
    True

    Be sure that equal(u, v) check equalities for all keys from u.f and v.f even if
    some keys in u.f do not exist in v.f (or vice versa)

    >>> Vec({'x','y','z'},{'y':1,'x':2}) == Vec({'x','y','z'},{'y':1,'z':0})
    False
    >>> Vec({'a','b','c'}, {'a':0,'c':1}) == Vec({'a','b','c'}, {'a':0,'c':1,'b':4})
    False
    >>> Vec({'a','b','c'}, {'a':0,'c':1,'b':4}) == Vec({'a','b','c'}, {'a':0,'c':1})
    False

    The keys matter:
    >>> Vec({'a','b'},{'a':1}) == Vec({'a','b'},{'b':1})
    False

    The values matter:
    >>> Vec({'a','b'},{'a':1}) == Vec({'a','b'},{'a':2})
    False

    >>> v1 = Vec({'a','b','c','d'}, {'a':2,      'c':1,'d':4})

    >>> Vec(set(),{}) == Vec(set(),{})
    True
    >>> v2 = Vec({'a','b','c','d'}, {'a':2,'b':0,'c':1,'d':4})
    >>> v3 = Vec({'a','b','c','d'}, {'b':1,'a':2,'c':1,'d':4})
    >>> v4 = Vec({'a','b','c','d'}, {'a':3,      'c':1,'d':4})
    >>> v5 = Vec({'a','b','c','d'}, {            'c':1,'d':4})
    >>> print(test_format((v1 == v1), 2))
    True
    >>> print(test_format((v1 == v2), 2))
    True
    >>> print(test_format((v2 == v1), 2))
    True
    >>> print(test_format((v1 == v3), 2))
    False
    >>> print(test_format((v3 == v1), 2))
    False
    >>> print(test_format((v1 == v4), 2))
    False
    >>> print(test_format((v1 == v5), 2))
    False
    >>> print(test_format((Vec({True, False}, {True: 1}) == Vec({True, False}, {False: 0})), 2))
    False
    >>> print(test_format((Vec({1, 3}, {1: 1, 3: 2}) == Vec({1, 3}, {1: 2, 3: 1})), 2))
    False
    >>> print(test_format((Vec({i for i in range(10)}, {i: 0 for i in range(4,8)}) == Vec({i for i in range(10)}, {})), 2))
    True
    >>> print(test_format((Vec({i for i in range(10)}, {}) == Vec({i for i in range(10)}, {i: 0 for i in range(1,3)})), 2))
    True
    >>> print(test_format((Vec(set(),{}) == Vec(set(),{})), 2))
    True
    """
    assert u.D == v.D
    equal = True

    for k in u.D:
        value_u = u[k]
        value_v = v[k]
        if value_u!=value_v:
            equal = False
            break

    return equal

def add(u,v):
    """
    Returns the sum of the two vectors.
    Make sure to add together values for all keys from u.f and v.f even if some keys in u.f do not
    exist in v.f (or vice versa)

    >>> a = Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2})
    >>> b = Vec({'a','e','i','o','u'}, {'o':4,'u':7})
    >>> c = Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2,'o':4,'u':7})
    >>> a + b == c
    True
    >>> a == Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2})
    True
    >>> b == Vec({'a','e','i','o','u'}, {'o':4,'u':7})
    True
    >>> d = Vec({'x','y','z'}, {'x':2,'y':1})
    >>> e = Vec({'x','y','z'}, {'z':4,'y':-1})
    >>> f = Vec({'x','y','z'}, {'x':2,'y':0,'z':4})
    >>> d + e == f
    True
    >>> b + Vec({'a','e','i','o','u'}, {}) == b
    True
    >>> Vec({1,2,3}, {1:1}) + Vec({1,2,3}, {2:2})
    Vec({1, 2, 3},{1: 1, 2: 2, 3: 0})
    >>> Vec({1,2,3}, {}) + Vec({1,2,3}, {2:2})
    Vec({1, 2, 3},{1: 0, 2: 2, 3: 0})
    >>> Vec({1,2,3}, {2:2}) + Vec({1,2,3}, {})
    Vec({1, 2, 3},{1: 0, 2: 2, 3: 0})
    >>> Vec({1,2,3}, {2:2}) + Vec({1,2,3}, {1:1, 2:2})
    Vec({1, 2, 3},{1: 1, 2: 4, 3: 0})
    >>> Vec({1}, {2:2}) + Vec({1}, {1:1, 2:2})
    Vec({1},{1: 1})
    >>> u = Vec({'a','b'},{'a':1})
    >>> v = Vec({'a','b'},{'b':2})
    >>> w1 = u + v
    >>> print(test_format(([u['a'], u['b']]), 2))
    [1.00, 0.00]
    >>> print(test_format(([v['a'], v['b']]), 2))
    [0.00, 2.00]
    >>> w2 = v + u
    >>> print(test_format(([w1['a'], w1['b']]), 2))
    [1.00, 2.00]
    >>> print(test_format(([w2['a'], w2['b']]), 2))
    [1.00, 2.00]
    >>> w3 = w1 + w1 + u
    >>> print(test_format(([w3['a'], w3['b']]), 2))
    [3.00, 4.00]
    >>> u2 = u + Vec(u.D, {})
    >>> print(test_format(([u2['a'], u2['b']]), 2))
    [1.00, 0.00]
    >>> print(test_format((Vec({'a','b'}, {'a':1})+Vec({'a','b'}, {'a':2})), 2))
    Vec({'a', 'b'}, {'a': 3.00})
    """
    assert u.D == v.D
    ret = Vec(u.D, {})
    for k in u.D:
        ret.f[k] = u[k]+v[k]
    return ret

def dot(u,v):
    """
    Returns the dot product of the two vectors.

    >>> u1 = Vec({'a','b'}, {'a':1, 'b':2})
    >>> u2 = Vec({'a','b'}, {'b':2, 'a':1})
    >>> u1*u2
    5
    >>> u1 == Vec({'a','b'}, {'a':1, 'b':2})
    True
    >>> u2 == Vec({'a','b'}, {'b':2, 'a':1})
    True
    >>> v1 = Vec({'p','q','r','s'}, {'p':2,'s':3,'q':-1,'r':0})
    >>> v2 = Vec({'p','q','r','s'}, {'p':-2,'r':5})
    >>> v1*v2
    -4
    >>> w1 = Vec({'a','b','c'}, {'a':2,'b':3,'c':4})
    >>> w2 = Vec({'a','b','c'}, {'a':12,'b':8,'c':6})
    >>> w1*w2
    72

    The pairwise products should not be collected in a set before summing
    because a set eliminates duplicates
    >>> v1 = Vec({1, 2}, {1 : 3, 2 : 6})
    >>> v2 = Vec({1, 2}, {1 : 2, 2 : 1})
    >>> v1 * v2
    12
    >>> u = Vec({'a','b','c'}, {})
    >>> v = Vec({'a','b','c'}, {'a': 1, 'b': 2})
    >>> w = Vec({'a','b','c'}, {'c': 1, 'b': 3})
    >>> x = Vec({'a','b','c'}, {'a': -1, 'c': 1, 'b': 3})
    >>> dot(u, u)
    0
    """
    assert u.D == v.D
    dot = 0
    for k in u.D:
        dot = dot + u[k]*v[k]
    return dot


def scalar_mul(v, alpha):
    """
    Returns the scalar-vector product alpha times v.

    >>> zero = Vec({'x','y','z','w'}, {})
    >>> u = Vec({'x','y','z','w'},{'x':1,'y':2,'z':3,'w':4})
    >>> 0*u == zero
    True
    >>> 1*u == u
    True
    >>> 0.5*u == Vec({'x','y','z','w'},{'x':0.5,'y':1,'z':1.5,'w':2})
    True
    >>> u == Vec({'x','y','z','w'},{'x':1,'y':2,'z':3,'w':4})
    True
    """
    ret = Vec(v.D, {})
    for k in v.f.keys():
        ret.f[k] = alpha*v.f[k]
    return ret

def neg(v):
    """
    Returns the negation of a vector.

    >>> u = Vec({2,4,6,8},{2:1,4:2,6:3,8:4})
    >>> -u
    Vec({8, 2, 4, 6},{8: -4, 2: -1, 4: -2, 6: -3})
    >>> u == Vec({2,4,6,8},{2:1,4:2,6:3,8:4})
    True
    >>> -Vec({'a','b','c'}, {'a':1}) == Vec({'a','b','c'}, {'a':-1})
    True
    >>> u = -Vec({'a','b','c'}, {})
    >>> v = -Vec({'a','b','c'}, {'a': 1, 'b': 2})
    >>> print(test_format(([(-u)[x] for x in 'abc']), 2))
    [0.00, 0.00, 0.00]
    >>> print(test_format(([(-v)[k] for k in 'abc']), 2))
    [1.00, 2.00, 0.00]
    >>> print(test_format(([v[k] for k in 'abc']), 2))
    [-1.00, -2.00, 0.00]
    >>> print(test_format(([(-(-v))[x] for x in 'abc']), 2))
    [-1.00, -2.00, 0.00]
    >>> print(test_format((-Vec({'A','B'}, {'A':1})), 2))
    Vec({'A', 'B'}, {'A': -1.00})
    >>> print(test_format((u['a']), 2))
    0.00
    >>> print(test_format((v['b']), 2))
    -2.00
    """
    return -1*v

###############################################################################################################################

class Vec:
    """
    A vector has two fields:
    D - the domain (a set)
    f - a dictionary mapping (some) domain elements to field elements
        elements of D not appearing in f are implicitly mapped to zero
    """
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    __neg__ = neg
    __rmul__ = scalar_mul #if left arg of * is primitive, assume it's a scalar

    def __mul__(self,other):
        #If other is a vector, returns the dot product of self and other
        if isinstance(other, Vec):
            return dot(self,other)
        else:
            return NotImplemented  #  Will cause other.__rmul__(self) to be invoked

    def __truediv__(self,other):  # Scalar division
        return (1/other)*self

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with vectors"
        if other == 0:
            return self

    def __sub__(a,b):
        "Returns a vector which is the difference of a and b."
        return a+(-b)

    __eq__ = equal

    def is_almost_zero(self):
        s = 0
        for x in self.f.values():
            if isinstance(x, int) or isinstance(x, float):
                s += x*x
            elif isinstance(x, complex):
                s += x*x.conjugate()
            else: return False
        return s < 1e-20

    def __str__(v):
        "pretty-printing"
        D_list = sorted(v.D, key=repr)
        numdec = 3
        wd = dict([(k,(1+max(len(str(k)), len('{0:.{1}G}'.format(v[k], numdec))))) if isinstance(v[k], int) or isinstance(v[k], float) else (k,(1+max(len(str(k)), len(str(v[k]))))) for k in D_list])
        s1 = ''.join(['{0:>{1}}'.format(str(k),wd[k]) for k in D_list])
        s2 = ''.join(['{0:>{1}.{2}G}'.format(v[k],wd[k],numdec) if isinstance(v[k], int) or isinstance(v[k], float) else '{0:>{1}}'.format(v[k], wd[k]) for k in D_list])
        return "\n" + s1 + "\n" + '-'*sum(wd.values()) +"\n" + s2

    def __hash__(self):
        "Here we pretend Vecs are immutable so we can form sets of them"
        h = hash(frozenset(self.D))
        for k,v in sorted(self.f.items(), key = lambda x:repr(x[0])):
            if v != 0:
                h = hash((h, hash(v)))
        return h

    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.f) + ")"

    def copy(self):
        "Don't make a new copy of the domain D"
        return Vec(self.D, self.f.copy())
