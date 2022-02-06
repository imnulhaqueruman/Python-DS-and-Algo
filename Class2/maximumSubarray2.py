class Solution:
    def maxSubArray(self,nums) -> int:
        self.nums = nums
        maxSum = -1e8
        currentSum = 0 
        n = len(nums) 
        for i in range(0, n):
            currentSum = currentSum + nums[i]
            if(maxSum < currentSum):
                maxSum = currentSum
            if(currentSum < 0):
                currentSum = 0
        return maxSum
p = Solution()
s = p.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(s)