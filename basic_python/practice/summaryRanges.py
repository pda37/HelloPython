def summaryRanges(nums):
    ans = []
    if len(nums) > 0:
        begin = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                end = nums[i-1]
                if begin == end:
                    ans.append(str(begin))
                else:
                    ans.append(str(begin)+'->'+str(end))
                begin = nums[i]
        if begin == nums[-1]:
            ans.append(str(begin))
        else:
            ans.append(str(begin) + '->' + str(nums[-1]))
    return ans


print(summaryRanges([0,2,3,4,6,8]))