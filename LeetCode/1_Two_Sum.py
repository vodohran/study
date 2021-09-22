# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
	temp = []
	for i, item in enumerate(nums):
		if item in temp: 
			return [nums.index(target - item),i]
		temp.append(target - item)
	return [110,110]

print(twoSum([2,7,11,15], 18))

