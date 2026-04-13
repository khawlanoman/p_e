def merge_and_sum(list1, list2):
    new_list={}
    
    for key, value in list1.items():
        new_v= value
        for k, v in list2.items():
            if key == k:
                new_v += v

            new_list[key]= new_v
    return new_list

first = {"a": 1, "b": 2}
second = {"b": 3, "c": 4}
print(merge_and_sum(first, second))
# {"a": 1, "b": 5, "c": 4}
first = {"gold": 10, "wood": 5}
second = {"wood": 7, "stone": 3}
print(merge_and_sum(first, second))
# {"gold": 10, "wood": 12, "stone": 3}