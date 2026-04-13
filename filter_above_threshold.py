def filter_above_threshold(data, t):
    new_dic={}
    for key,value in data.items():
        if value > t:
            new_dic[key]=value
    
    return new_dic

data = {"a": 1, "b": 5, "c": 3}
threshold = 2
print(filter_above_threshold(data, threshold))
# {"b": 5, "c": 3}

print(filter_above_threshold({"x": 10, "y": 2, "z": 10}, 10))
# {}  (no values strictly greater than 10)

print(filter_above_threshold({}, 5))
# {}
