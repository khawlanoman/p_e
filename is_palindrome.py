def is_palindrome(s):
    
    l=s.replace(" ","")[::-1]
    s = s.replace(" ","")
    if s.lower() != l.lower():
        return False
    return True
    

print(is_palindrome("A man a plan a canal Panama"))
# True

print(is_palindrome("Boot dev"))
# False

print(is_palindrome("No lemon, no melon"))
# True