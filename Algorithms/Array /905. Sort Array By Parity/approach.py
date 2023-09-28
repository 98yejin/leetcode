class Solution:
    # use sorted (key)
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x%2)
    
    # list comprehension
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [num for num in nums if not num%2] + [num for num in nums if num%2]
    
    # two pointers (in-place, quicksort)
    def sortArrayByParity(self, nums: List[int]) -> List[int]:        
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums

    # in-place
    def sortArrayByParity(self, nums: List[int]) -> List[int]:        
        last_even_index = -1
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                last_even_index += 1
                nums[i], nums[last_even_index] = nums[last_even_index], nums[i]
        return nums