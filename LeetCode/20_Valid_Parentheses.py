# def isValid(s):
# 
# 	
# 	for i in range(len(s)):
# 		s = s.replace("()",'')
# 		s = s.replace("{}",'')
# 		s = s.replace("[]",'')
# 	return stack == []


def isValid(s):
	stack = []
	
	skobka_close = {")":"(", "}":"{","]":"["}
	for i in s:
		
		if (i in skobka_close) and (len(stack)>0) and (stack[-1] == skobka_close[i]):
			stack.pop()
		else:
			stack.append(i)

	print(stack)		
	return stack == []



print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
print(isValid("]))"))


