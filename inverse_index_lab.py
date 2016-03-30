# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

import random
import dictutil


## 1: (Task 1) Movie Review
## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    reviews = ["See it!", "A gem!", "Ideological claptrap!", "its awesome", "Don't see it ever", "wow!", "what a joke"]
    return reviews[random.randint(0, len(reviews)-1)]

print("Star wars review: ", movie_review("asdf"))
print("Listrange2dict: ", dictutil.listrange2dict(['A', 'B', 'C']))

## 2: (Task 2) Make Inverse Index
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
    invIndex = {}
    strlist_enum = list(enumerate(strlist))
    for (i, document) in strlist_enum:
        doc_split = list(document.split())
        for word in doc_split:
            if word in invIndex:
                invIndex[word].add(i)
            else:
                invIndex[word] = {i}
    return invIndex

def loadFromfile(fileName):
    f = open(fileName)
    return list(f)

print("InvIndex: ", makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']))
print("File inv index: ", makeInverseIndex(loadFromfile("stories_small.txt")))



## 3: (Task 3) Or Search
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
    """
    orDoc_set = set({})
    for word in query:
        if word in inverseIndex:
            doc_set =  inverseIndex[word]
            for doc_num in doc_set:
                orDoc_set.add(doc_num)
    return orDoc_set

idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
print("orSearch", orSearch(idx, ['Johann', 'Carl']))
print("orSearch", orSearch(idx, ['Bach', 'the']))

## 4: (Task 4) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """

    andDoc_set = set({})
    doc_list = []
    for word in query:
        if word in inverseIndex:
            doc_list.append(inverseIndex[word])
    andDoc_set = doc_list[1]
    for doc_set in doc_list:
        andDoc_set = andDoc_set.intersection(doc_set)

    return andDoc_set

idx2 = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
print("And search: ", andSearch(idx2, ['Johann', 'the']))

print("And searc: ", andSearch(idx2, ['Johann', 'Bach']))
