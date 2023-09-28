class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                count += (i - stack[-1]) # (next smaller index - current index) = number of valid subarrays that begins at the current index i
                stack.pop()
            stack.append(i)
        while stack:
            count += (n - stack[-1])
            stack.pop()
        return count