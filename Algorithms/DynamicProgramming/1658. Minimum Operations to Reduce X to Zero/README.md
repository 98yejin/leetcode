# 1658. Minimum Operations to Reduce X to Zero

## initial thoughts

```none
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1
```

- `the minimum number of operations to reduce x to exactly 0` equals `make x using minimum number of elements`
- `the minimum number of operations` -> greedy or dp
- `you can either remove the leftmost or the rightmost element from the array`
  - there's no *overlapping* subprobem, so use *greedy*
- `leftmost or rightmost` -> use two pointers/sliding window
