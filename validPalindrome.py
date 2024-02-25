def validPalindrome(s,a=""):    
    for i in s:
        if i.isalnum():
            a +=  "".join(i.lower())
            
    return a == a[::-1]
###
s = "A man, a plan, a canal: Panama"
print(validPalindrome(s))