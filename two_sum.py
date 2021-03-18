# O(n^2)
# def twoSum(nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]
# O(n)
def twoSum(nums, target):
         vals = dict()
        for i in range(len(nums)):
            val = vals.get(nums[i])
            if(val is not None):
                return [val, i]
            else:
                vals[target-nums[i]] = i
# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,4],6))
# print(twoSum([3,3], 6))
print(twoSum([-1,-2,-3,-4,-5], -8))