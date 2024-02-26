def twoSum2(numbers,target = 9):
    l = 0
    r = len(numbers)-1
    while r>l:
        if (numbers[l]+numbers[r]>target):
            r -= 1
        elif (numbers[l]+numbers[r]<target):
            l += 1
        else:
            return [l+1,r+1]

testCases = [
    [0,1,2,4,5,6],
    [-1,-1,-1,-1,4,5],
    [0,1,2,2,3,5,5,6]
    
]    

for nums in testCases:
    print(twoSum2(nums))


