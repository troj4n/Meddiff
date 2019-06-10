# coding: utf-8
# Your code here!
#Using Python 2.7

def check_palindrome(s):
    s=str(s).lower()
    if (s==s[::-1]):
        return "Yes"
    else:
        return "No"
word="rahuluhar"
print check_palindrome(word)