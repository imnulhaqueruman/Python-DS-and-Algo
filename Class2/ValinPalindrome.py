def validPalindrome(s):
    start = 0
    end  = len(s) - 1
    while start < end :
        if(s[start] != s[end]):
            return print(False) 
        start += 1
        end -= 1
    return print(True)

str = 'MADAM'
validPalindrome(str)