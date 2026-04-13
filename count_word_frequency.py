def count_word_frequency(s_str):
    new_list = s_str.split()
    new_dic ={}
    list_len=[]
    count = 0
    for k in new_list:
       count = 0
       for j in new_list:
            if j == k :
                count+=1
       new_dic[k]=count

    return new_dic

sentence = "hello world hello"
print(count_word_frequency(sentence))
# {"hello": 2, "world": 1}

sentence = "one two two three three three"
print(count_word_frequency(sentence))
# {"one": 1, "two": 2, "three": 3}
sentence = ""
print(count_word_frequency(sentence))
# {}