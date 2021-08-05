# solving useing Nested Loop 
# Time complexity O(n^2)
# Space complexity O(1)
class Solution:
    def twoSum(self,nums,target):
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if(nums[x] + nums[y] == target):
                    return(x,y)