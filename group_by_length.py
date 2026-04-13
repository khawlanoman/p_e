def group_by_length(s_list):

    new_dic = {}
    len_value= []
   
    for i in s_list:
        len_value.append(len(i))
    
    for l in len_value:
        list_t =[]
        for k in s_list:
            if len(k) == l:
                list_t.append(k)
        new_dic[l]=list_t


    return new_dic
   
    

words = ["a", "bb", "ccc", "dd"]
print(group_by_length(words))
# {1: ["a"], 2: ["bb", "dd"], 3: ["ccc"]}

words = ["", "hi", "a", "hey", ""]
print(group_by_length(words))
# {0: ["", ""], 2: ["hi"], 1: ["a"], 3: ["hey"]}