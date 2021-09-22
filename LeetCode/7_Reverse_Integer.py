# https://leetcode.com/problems/reverse-integer/
def reverse(x):
	temp = 0
	if (x >= pow(2,31) -1) or (x <= -1* pow(2, 31)): return 0
	if x>0: temp = int(str(x)[::-1])
	if x<0: temp = (-1) * int(str(-1*x)[::-1])
	if (temp >= pow(2,31) -1) or (temp <= -pow(2, 31)): return 0
	return temp

print(reverse(16469))

