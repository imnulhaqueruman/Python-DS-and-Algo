class Solution:
    def maxSubArray(self,nums) -> int:
        self.nums = nums
        maxSum = -1e8
        n = len(nums)
        for i in range(0, n):
            currentSum = 0
            for j in range(i, n):
                currentSum = currentSum + nums[j]
                if(currentSum>maxSum):
                    maxSum = currentSum
        return maxSum
p = Solution()
s = p.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])
print(s)
