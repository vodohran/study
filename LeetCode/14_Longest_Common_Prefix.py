strs = ["flower","flow","floight"]

min_word = min(len(x) for x in strs)
n = 0

for i in range(min_word):
	new_str = [x[:i+1] for x in strs]
	if new_str.count(new_str[0]) == len(strs): n = i+1;
	#print("new_str = ", new_str)
	print("n = ",n)


print(strs[0][:n])



