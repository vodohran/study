def removeElement(nums, val):
    count_val_in_nums = nums.count(val)
    for i in range(count_val_in_nums): nums.remove(val)
    return len(nums), nums

print(removeElement([3,2,2,3,5],3))