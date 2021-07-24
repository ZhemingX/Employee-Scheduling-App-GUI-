import random

# some ops for list

# split list according to steps
def list_split(l, step):
    # step: split length
    if len(l) <= step:
        return l
    start = 0
    list_len = len(l)
    res = []
    while list_len - 1 - start + 1 > step:
        res.append(l[start:start+step])
        start += step
    res.append(l[start:])

    return res

#print(list_split([i for i in range(31)], 5))

# combine 2 lists into a dict, with value list has a random order
def list_to_dict(l1, l2):
    random.shuffle(l2)
    return dict(zip(l1, l2))

#print(list_to_dict(["aa","dd","cc"], [1,2,3]))

