'''Machine Problem #2
1. create a function that accepts a string 
2. return a boolean if it is a palindrome or not
'''

def is_palindrome(text):
    r=text[::-1]
    for i in range (0, (len(text)-1)/2):
        if r[i] != text[i]:
            return False
    return True

print(is_palindrome("mimim"))