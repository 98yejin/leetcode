# [896. Monotonic Array](https://leetcode.com/problems/monotonic-array)

## one pass iteration

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = is_decreasing = True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                is_decreasing = False
            elif nums[i] > nums[i+1]:
                is_increasing = False
        return is_increasing or is_decreasing
```

Start by initializing two flags, is_increasing and is_decreasing, as True. Then, iterate through the array from the second element to the last element and compare each element with the previous one. Update the flags accordingly. If at any point, both is_increasing and is_decreasing become False, you can return False immediately since the array is neither increasing nor decreasing. Otherwise, return True at the end of the loop.

## two pass iteration

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return (all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or all(nums[i] >= nums[i+1] for i in range(len(nums)-1)))
```

Checks if either of the two conditions is satisfied for all adjacent pairs of elements in the input nums list. If either condition holds true for all adjacent pairs, it means that the list is either monotonic increasing or monotonic decreasing, and the function returns True. Otherwise, if both conditions fail for any pair, the function returns False, indicating that the list is neither monotonic increasing nor monotonic decreasing.

## sort and compare

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)
```

Create two sorted versions of the array: one in ascending order and one in descending order. Then, compare these sorted arrays with the original array. If either of the sorted arrays matches the original array, it's monotonic.

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] == nums[-1]:
            return nums == sorted(nums)
        if nums[0] < nums[-1]:
            return nums == sorted(nums)
        return nums == sorted(nums, reverse=True)
```

Check before sort the array.
