# version code 6adf56d2e064+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.




## 1: (Task 2.12.1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    ret = {}
    for str in strlist:
        info = str.split()
        senator_name = info[0]
        vote_list = []
        for i in range(3, len(info)):
            vote_list.append(int(info[i]))
        ret[senator_name] = vote_list
    return ret



## 2: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    dot = 0
    for i in range(len(voting_dict[sen_a])):
        dot = dot + voting_dict[sen_a][i]*voting_dict[sen_b][i]
    return dot



## 3: (Task 2.12.3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'
        >>> vd == {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        True
        >>> vd = {'a': [1,1,1,0], 'b': [1,-1,0,0], 'c': [-1,0,0,0], 'd': [-1,0,0,1], 'e': [1, 0, 0,0]}
        >>> most_similar('c', vd)
        'd'

    Note that you can (and are encouraged to) re-use your policy_compare procedure.
    """
    max_score = float('-inf')
    max_sen = ""
    for name in voting_dict.keys():
        if name!=sen:
            score = policy_compare(sen, name, voting_dict)
            if score>max_score:
                max_score = score
                max_sen = name

    return max_sen



## 4: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
        >>> vd == {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        True
        >>> vd = {'a': [-1,0,0], 'b': [1,0,0], 'c': [-1,1,0], 'd': [-1,1,1]}
        >>> least_similar('c', vd)
        'b'
    """
    min_score = float('inf')
    min_sen = ""
    for name in voting_dict.keys():
        if name!=sen:
            score = policy_compare(sen, name, voting_dict)
            if score<min_score:
                min_score = score
                min_sen = name

    return min_sen



## 5: (Task 2.12.5) Chafee, Santorum
f = open('voting_record_dump109.txt')
voting_strlist = list(f)
voting_dict = create_voting_dict(voting_strlist)
most_like_chafee    = most_similar('Chafee', voting_dict)
least_like_santorum = least_similar('Santorum', voting_dict)

print(most_like_chafee)
print(least_like_santorum)



## 6: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
        >>> find_average_similarity('Klein', sens, vd)
        -0.5
        >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
        True
        >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        True
    """
    total_dot = 0
    for senator in sen_set:
        if(senator!=sen):
            total_dot = total_dot + policy_compare(sen, senator, voting_dict)

    return total_dot/len(sen_set)

def get_democratic_names(voting_strlist):
    ret = []
    for str in voting_strlist:
        str_list = str.split()
        if str_list[1]=='D':
            ret.append(str_list[0])
    return ret

def highest_avg_democrat(voting_strlist):
    max_avg=float('-inf')
    most_avg_democrat = ''
    democrat_list = get_democratic_names(voting_strlist)
    for sen in democrat_list:
        avg = find_average_similarity(sen, set(democrat_list), voting_dict)
        if avg>max_avg:
            max_avg = avg
            most_avg_democrat = sen
    return most_avg_democrat

most_average_Democrat = highest_avg_democrat(voting_strlist) # give the last name (or code that computes the last name)

print(most_average_Democrat)



## 7: (Task 2.12.8) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> senators = {'Fox-Epstein','Ravella'}
        >>> find_average_record(senators, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        True
        >>> senators
        {'Fox-Epstein', 'Ravella'}
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    sum_record = []
    count=0
    for sen in sen_set:
        if count==0:
            sum_record = list(voting_dict[sen])
            count = count+1
            continue;
        for i in range(len(voting_dict[sen])):
            sum_record[i] = sum_record[i]+voting_dict[sen][i]
        count = count + 1


    return [value/count for value in sum_record]


democrat_list = get_democratic_names(voting_strlist)

average_Democrat_record = find_average_record(set(democrat_list), voting_dict) # give the vector as a list



## 8: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein')
        True
    """
    rival_score = float('inf')
    sen1 = ''
    sen2 = ''
    for sen_1 in voting_dict.keys():
        sen_2 = least_similar(sen_1, voting_dict)
        score = policy_compare(sen_1, sen_2, voting_dict)
        if score < rival_score:
            rival_score = score
            sen1 = sen_1
            sen2 = sen_2

    return (sen1, sen2)

