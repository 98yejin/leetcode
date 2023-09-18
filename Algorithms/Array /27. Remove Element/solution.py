class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader, writer = 0, 0
        n = len(nums)
        while reader < n:
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1
            reader += 1
        return writer

