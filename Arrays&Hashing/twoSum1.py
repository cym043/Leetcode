# The first thing that comes in mind is a ,
# time = O(n²) space = O(1) solution. 
# But its possible to reduce it by storing information inside a Map/Dict so the complexitiy becomes,
# time = O(n) space = O(n).

def twoSum(nums, target):
    adict = {}
    for i in range(len(nums)):
        num = target - nums[i]
        if num in adict:
            return [adict[target - nums[i]] , i]
        else:
            adict[nums[i]] = i
    return []
        
print(twoSum([3,2,4],6))