# 287. Find the Duplicate Number

## Space Complexity

- constant space complexity `O(1)` : no loop, recursive function, or call to any other functions.
- linear space complexity `O(n)`

## Floyd's Tortoise and Hare

This algorithm is designed to detect cycles in a linked list, but it can also be applied to this problem since the repeated number effectively creates a cycle in the array.

1. Initialize two pointers, slow and fast, both initially pointing to the first element of the array (nums[0]).
2. Move the slow pointer one step at a time, and the fast pointer two steps at a time until they meet inside the cycle. This is guaranteed to happen because of the repeated number.
3. Once they meet, reset the slow pointer to the beginning of the array while keeping the fast pointer where it is.
4. Move both pointers one step at a time until they meet again. The point where they meet is the entrance to the cycle, which is also the repeated number.
