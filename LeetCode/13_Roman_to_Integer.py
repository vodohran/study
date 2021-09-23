# https://leetcode.com/problems/roman-to-integer/

def romanToInt(s):
	Romans = {	"I":1, 
			"V":5,
			"X":10,
			"L":50,
			"C":100,
			"D":500,
			"M":1000}
	s = s[::-1]
	sum = Romans[s[0]]
	for i in range(1,len(s)):
		if Romans[s[i]] >= Romans[s[i-1]]:
			sum = sum + Romans[s[i]]
		else:
			sum = sum - Romans[s[i]]
	return sum

print(romanToInt("IX"))