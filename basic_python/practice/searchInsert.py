def searchInsert(nums, target):
    if target <= nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    else:
        left_index = 0
        right_index = len(nums) - 1
        mid_index = int((left_index+right_index)/2)
        while left_index + 1 < right_index:
            if nums[mid_index] > target:
                right_index = mid_index
                mid_index = int((left_index + right_index) / 2)
            elif nums[mid_index] < target:
                left_index = mid_index
                mid_index = int((left_index + right_index) / 2)
            else:
                return mid_index
        return mid_index + 1


print(searchInsert([1,6], 6))