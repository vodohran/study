# https://leetcode.com/problems/search-insert-position/submissions/
# бинарный поиск


def searchInsert( nums, target):
        current_index = 0
        left_index = 0
        right_index = len(nums)-1
        while (left_index <= right_index):
                mid = (left_index+right_index) // 2
                if target == nums[mid]: return mid
                if target > nums[mid]:
                        left_index = mid + 1
                else:
                        right_index = mid - 1
        return left_index

nums = [1,3,5,6]
target = 5
print(searchInsert(nums,target))