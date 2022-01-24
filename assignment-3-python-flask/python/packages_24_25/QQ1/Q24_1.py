### module for Q24_2.py

def reverseStr(s):
    return s[::-1]

def checkPalindrome(s):
    return f"String is Palindrome is {s == s[::-1]}"

def evenOdd(n):
    if n%2==0:
        return "Number is even"
    return "Number is odd"