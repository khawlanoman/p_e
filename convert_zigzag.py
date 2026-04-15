def convert_zigzag(s1, num):
    m_list =[]
    new_str=""
    for i in  range(num):
            c_list = []
            for j in range(1):
                c_list.append("#")
            m_list.append(c_list)
    k = 1
    i = 0
    if num <=1:
         return (s1)
    for l in s1:
        m_list.append(l)
        i +=k

        if i == len(m_list) -1:
              k = -1
        else:
             k = 1

    for i in m_list:
         for k in i:
            if k != "#":
                new_str += k
    return (new_str)   

print(convert_zigzag("PAYPALISHIRING", 3))
# "PAHNAPLSIIGYIR"

print(convert_zigzag("HELLOPYTHON", 4))
# "HYEPTLOHNLO"

print(convert_zigzag("ABC", 1))
# "ABC" (no change, only one row)