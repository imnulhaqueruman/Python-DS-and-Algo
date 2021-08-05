# Time complexity O(N)
# Space complexity O(1)
class Solution:
    def twoSum(self, nums, target):
        container = {}
        for x,y in enumerate(nums):
            if target - y in container:
                return[container[target-y],x]
            container[y] = x