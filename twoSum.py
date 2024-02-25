def twoSum(nums,target=10):
    x=0
    while x<len(nums):
        for i in range(x+1,len(nums)):
            if (nums[x]+nums[i] == target):
                return [x,i]
        x+=1
###
testCases = [
    [2,8,11,15],
    [3,2,7],
    [2,5,5,11]
    ]
###
for nums in testCases:
    print(twoSum(nums))