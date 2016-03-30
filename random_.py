#define a procedue that will add two vectors
def add(v, w):
    return [v[i]+w[i] for i in range(len(v))]

print("addVectors: ", add([1,2], [3,4]))

class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def setitem(self, d, val):
        self.f[d] = val

    def getitem(self, d):
        return self.f[d] if d in self.f else 0

v = Vec({'A', 'B', 'C'}, {'A':1, 'B':2, 'C':3})
print("Element A: ", v.getitem('A'))
v.setitem('A', 4)
print("Element A: ", v.getitem('A'))

def list2vec(L):
    return Vec(set(range(len(L))), {i:L[i] for i in range(len(L))})

v = list2vec([1, 2, 3, 4, 5, 6])
print(v.getitem(0))

def list_dot(u, v):
    return sum([u[i]*v[i] for i in range(len(v))])

print("Dot product: ", list_dot([1,2], [3, 4]))

print("Matrix in python", [[0 for i in range(4)] for j in range(3)])

print("Matrix in Python2: ", [[i-j for j in range(4)] for i in range(3)])