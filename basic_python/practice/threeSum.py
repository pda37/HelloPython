def threeSum(nums):
    if len(nums) < 3:
        return []
    else:
        nums.sort()
        print(nums)
        nums_three = []
        smallest_two = nums[0] + nums[1]
        zero_index = len(nums) - 1
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                for j in range(i + 1, len(nums)-1):
                    if nums[i] + nums[j] > 0:
                        break
                    elif j-i > 1 and nums[j] == nums[j-1]:
                        continue
                    elif nums[i] + nums[j] < smallest_two:
                        for k in range(len(nums)-1, zero_index-1, -1):
                            if nums[i] + nums[j] + nums[k] < 0:
                                break
                            elif k-j > 1 and k < len(nums)-1 and nums[k] == nums[k+1]:
                                continue
                            elif nums[i] + nums[j] + nums[k] > 0:
                                continue
                            else:
                                nums_three.append([nums[i], nums[j], nums[k]])
                                zero_index = k
                                smallest_two = nums[i] + nums[j]
                                break
                    else:
                        for k in range(zero_index, j, -1):
                            if nums[i] + nums[j] + nums[k] < 0:
                                break
                            elif k-j > 1 and k < zero_index-1 and nums[k] == nums[k-1]:
                                continue
                            elif nums[i] + nums[j] + nums[k] > 0:
                                continue
                            else:
                                nums_three.append([nums[i], nums[j], nums[k]])
                                zero_index = k
                                smallest_two = nums[i] + nums[j]
                                break
        return nums_three


print(threeSum([-7,-4,-4,-2,0,4,4,5,7,7,9,9]))


# def threeSum(nums):
#     if len(nums) < 3:
#         return []
#     else:
#         nums.sort()
#         nums_three = []
#         for i in range(len(nums)-2):
#             left_index = i + 1
#             right_index = len(nums) - 1
#             if nums[i] > 0:
#                 break
#             elif i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             else:
#                 while left_index < right_index:
#                     three_sum = nums[i] + nums[left_index] + nums[right_index]
#                     if three_sum > 0:
#                         right_index -= 1
#                     elif three_sum < 0:
#                         left_index += 1
#                     elif three_sum == 0:
#                         nums_three.append([nums[i], nums[left_index], nums[right_index]])
#                         while right_index > left_index and nums[left_index] == nums[left_index + 1]:
#                             left_index += 1
#                         while left_index < right_index and nums[right_index] == nums[right_index - 1]:
#                             right_index -= 1
#                         left_index += 1
#                         right_index -= 1
#         return nums_three
#
#
# print(threeSum([0,0,0]))
