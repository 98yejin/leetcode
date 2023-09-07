# 169. Majority Element

## Problem

```None
Given an array nums of size n, return the majority element.

- The majority element is the element that appears more than ⌊n / 2⌋ times. 
- You may assume that the majority element always exists in the array.
```

## Approach

### Use Built-in Functions

Use Counter from collections. A Counter is a dict subclass for counting hashable objects.

- [collections](https://docs.python.org/3/library/collections.html)
  - [Counter](https://docs.python.org/3/library/collections.html#collections.Counter)
    - most_common(n) :  Return a list of the n most common elements and their counts from the most common to the least.

### Sorting

If the elements are sorted ( increasing / decreasing both are ok), the majority element can be found at index n//2.

### Boyer-Moore Voting Algorithm

The Boyer-Moore majority voting algorithm is an algorithm that can find elements that contain more than half of the elements in the array by linear time and constant space.
If it is guaranteed that a majority (more than half) of the elements in the array are present, the resulting value is always a majority element.
In this problem, the Boyer Moore voting algorithm can be used because it guarantees the presence of a majority (more than half) of elements in the array.

