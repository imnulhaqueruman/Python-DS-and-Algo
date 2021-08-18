# Remove Duplicate from Sorted Array 
def Duplicate (nums):
    k = 0
    for j in range(len(nums)):
        if(nums[j] != nums[k]):
            k += 1
            nums[k] = nums[j]
    return print(k+1)
arr = [1,1,2]
Duplicate(arr)
 