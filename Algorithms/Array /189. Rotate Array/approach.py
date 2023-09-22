class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = n - (k%n)
        nums[:] = nums[m:] + nums[:m]