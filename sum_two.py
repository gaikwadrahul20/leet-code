def twoSum(nums, target)
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            print(i,j)
    # return res

twoSum([2,7,11,15],9)