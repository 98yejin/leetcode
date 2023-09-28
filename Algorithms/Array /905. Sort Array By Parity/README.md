# 905. Sort Array By Parity

## sorted (lambda)

```python
sorted(nums, key=lambda x: x%2)
```

Both list.sort() and sorted() have a key parameter to specify a function (or other callable) to be called on each list element prior to making comparisons.

## two pointers

Initialize two pointers, left at the beginning of the array and right at the end of the array.
Iterate through the array while left < right:

- If nums[left] is even, increment left.
- If nums[right] is odd, decrement right.
- If nums[left] is odd and nums[right] is even, swap nums[left] and nums[right].

Continue this process until left >= right, and you will have all even numbers at the beginning and all odd numbers at the end of the array.

## list comprehension

Use list comprehensions to create two separate lists, one for even numbers and one for odd numbers.
Then concatenate these two lists to get the desired result.

## in-place

Use a single pointer to iterate through the array and keep track of the last even index.
Whenever encounter an even number, swap it with the element at the last even index and increment the last even index.
