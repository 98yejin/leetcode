class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        operations = -1

        current = left = 0 
        for right in range(len(nums)):
            current += nums[right]
            while (left <= right and current > total - x):
                current -= nums[left]
                left += 1
            if current == total - x:
                operations = max(operations, right-left+1)
        return -1 if operations == -1 else len(nums) - operations            
