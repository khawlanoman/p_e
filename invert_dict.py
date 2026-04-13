def invert_dict(d):
    new_dic = {}
    for key, value in d.items():
        new_dic[value] = key
    
    return new_dic

original = {"a": 1, "b": 2}
print(invert_dict(original))
# {1: "a", 2: "b"}

more_users = {"alice": 100, "bob": 200, "charlie": 300}
print(invert_dict(more_users))
# {100: "alice", 200: "bob", 300: "charlie"}