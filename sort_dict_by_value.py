def sort_dict_by_value(d):
    new_dict = sorted(d.values())
    new_dict = new_dict[::-1]
    
    new_list = []
    for i in new_dict:
        for key,value in d.items():
            if i == value:
                new_list.append((key, value))

    return new_list

scores = {"a": 3, "b": 1, "c": 2}
print(sort_dict_by_value(scores))
# [('a', 3), ('c', 2), ('b', 1)]

empty = {}
print(sort_dict_by_value(empty))
# []

more_scores = {"alice": 10, "bob": 15, "carol": 12}
print(sort_dict_by_value(more_scores))
# [('bob', 15), ('carol', 12), ('alice', 10)]