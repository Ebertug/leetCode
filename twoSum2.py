def twoSum(nums,target=2):
    x=0
    for x in range(len(nums)):
        for i in range(x+1,len(nums)):
            if (nums[x]+nums[i] == target):
                return [x+1,i+1]
        x+=1

def deleteDuplicate(nums,itemCounter=0):
    
    for x in range(0,len(nums)-1):
        if nums[x] == nums[x+1]:
            itemCounter += 1
        else:
            itemCounter = 0
            
        if itemCounter > 2:
            nums.pop(x)
        
    print(twoSum(nums))
###
nums = [-1,-1,-1,-1,1,1]
###
deleteDuplicate(nums)

