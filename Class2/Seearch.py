#Search Insert Position 
def search(nums, target):
    k= 0 
    for j in range(len(nums)):
        if nums[-1] < target : 
            return print(len(nums))
        elif nums[j] == target: 
            return print(j)
        elif nums[j] < target : 
            k += 1
        else : 
            return print(k)
arr = [1,3,5,6]
target = 7
search(arr,target)