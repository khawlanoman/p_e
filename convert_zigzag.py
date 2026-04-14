def convert_zigzag(s1, num):
    m_list =[]
    new_str=""
    for i in  range(num):
            c_list = []
            for j in range(1):
                c_list.append("#")
            m_list.append(c_list)
    
    for l in s1:
        for i > 
    return (m_list)   

print(convert_zigzag("PAYPALISHIRING", 3))
# "PAHNAPLSIIGYIR"

print(convert_zigzag("HELLOPYTHON", 4))
# "HYEPTLOHNLO"

print(convert_zigzag("ABC", 1))
# "ABC" (no change, only one row)