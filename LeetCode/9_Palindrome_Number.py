"""
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

"""
def isPalindrome(x):
        return  str(x) == str(x)[::-1]

print (isPalindrome(121))
print (isPalindrome(-121))
print (isPalindrome(13221))
print (isPalindrome(14541))