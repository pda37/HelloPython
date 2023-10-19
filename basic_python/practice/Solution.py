# # 表示该类是从哪个类继承而来的，所有类最终都会继承自 object 类
# class Solution(object):
#     def __init__(self, nums, target):
#         self.nums = nums
#         self.target = target
#
#     def twosum(self):
#         for i in range(len(self.nums)-1):
#             for j in range(i+1, len(self.nums)):
#                 if self.nums[i] + self.nums[j] == self.target:
#                     return [i, j]
#
#
# # 类对象支持两种操作：属性引用和实例化
# result = Solution([3, 2, 4, 100, 1000, 10000], 11000)  # 实例化
# result.twosum()  # 属性引用

# 两数之和
class Solution():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twosum(self):
        for i in range(len(self.nums)-1):
            for j in range(i + 1, len(self.nums)):
                two = self.nums[i] + self.nums[j]
                if two == self.target:
                    return [i, j]


result = Solution([3, 2, 4, 100, 1000, 10000, 100000], 1100)
print(result.twosum())

# def two(nums, target):
#     for i in range(len(nums)-1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
#
# result = two([3, 2, 4, 100, 1000, 10000, 100000], 5)
# print(result)
