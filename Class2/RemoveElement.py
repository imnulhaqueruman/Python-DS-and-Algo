'''Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

'''def removeElement(arr,val):
    k = 0 
    for j in range(len(arr)):
        if(arr[j] != val):
            arr[k] = arr[j]
            k += 1
    return print(k)
nums=[3,2,2,3]
val = 3
removeElement(nums,val)'''

# Two pointer approach 
def removeElement(arr,val):
    s = 0 
    e = len(arr)
    while s < e:
        if(arr[s] == val):
            arr[s] = arr[e-1]
            e -= 1
        else:
            s += 1
    return print(s)
nums=[3,2,2,3]
val = 3
removeElement(nums,val)