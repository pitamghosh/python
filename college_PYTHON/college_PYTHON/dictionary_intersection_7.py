# Dictionary Intersection

def dict_intersection(d1, d2):
    return {k: d1[k] for k in d1 if k in d2 and d1[k] == d2[k]}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

intersection_dict = dict_intersection(dict1, dict2)
print(intersection_dict)
