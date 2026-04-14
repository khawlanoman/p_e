def find_substring_ci(s1,s2):
    s1 = s1.lower()
    s2= s2.lower()
    if not s2:
        return (True,0)

    for  i in range(len(s1)):
        if i + len(s2) > len(s1):
            break

        m = True
        for j in range(len(s2)):
            if s1[i+j] != s2[j]:
                m = False
                break
            
        if m:
            return(True, i)

    return (False, -1)

print(find_substring_ci("Boot.dev Backend", "back"))
# (True, 9)

print(find_substring_ci("Dungeon Crawler", "crawl"))
# (True, 8)

print(find_substring_ci("Python", "thon"))
# (True, 2)

print(find_substring_ci("Python", "java"))
# (False, -1)

print(find_substring_ci("Any text", ""))
# (True, 0)