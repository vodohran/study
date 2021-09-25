# https://leetcode.com/problems/sqrtx/

def mySqrt(x):
        A = x // 2
        while (x - A*A)<0:
            A = (A + x // A) // 2
        return A  

print (mySqrt(170))