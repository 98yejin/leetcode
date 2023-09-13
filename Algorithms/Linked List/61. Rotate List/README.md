# 61. Roate List

## Apporach

### Base cases

```python3
    if not head or not head.next or not k:
        return head
```

- There's no condition regarding the lenght of the head
  - So, if the head is None or the length of the head is 1 (head.next is None), the rotated list is the same as the original list.
- k can be 0 (the range of k is `0 <= k <= 2 * 10^9`)

### Calculate the effective number of rotations (k % length) to handle cases where k is greater than the length of the list

```python3
    current = head
    length = 1
    while current.next:
        current = current.next
        length += 1
    k %= length 
    if not k: # we don't have to lotate the linked list
        return head
    current.next = head # make a circular linked list
```

### Traverse the list to find the new tail (the node that will become the new head after rotation) and the node just before it

```python3
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
```
