def twoSum(nums,target=2):
    x=0
    for x in range(len(nums)):
        for i in range(x+1,len(nums)):
            if (nums[x]+nums[i] == target):
                return [x+1,i+1]
        x+=1

def deleteDuplicate(nums,itemCounter=2):
    
    for x in range(0,len(nums)-3):
        if nums[x] == nums[x+1]:
            itemCounter += 1
        else:
            itemCounter = 0
            
        if itemCounter > 2:
            nums.pop(x+1)
        
    print(twoSum(nums))
###
nums = [1,1,1,1,2,3,4,5]
###
deleteDuplicate(nums)

