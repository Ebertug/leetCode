def containsDuplicate(self,nums):
    return not len(set(nums)) == len(nums)
###
testCases=[
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2]
]
###
for nums in testCases:
    containsDuplicate(nums)