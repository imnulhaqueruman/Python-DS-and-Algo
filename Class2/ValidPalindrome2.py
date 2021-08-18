#Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
def validPalindrome(s):
   
    start = 0
    end = len(s) - 1
    while start < end :
        if not s[start].lower().isalnum() :
            start += 1
        elif not s[end].lower().isalnum():
            end -= 1
        elif s[start].lower() != s[end].lower():
            return print(False) 
        else:
            start += 1
            end -= 1
    return print(True) 
str = "A man, a plan, a canal: Panama"
validPalindrome(str)