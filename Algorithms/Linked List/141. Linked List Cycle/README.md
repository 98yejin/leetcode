# 141. Linked List Cycle

## Problem

```None
Given head, the head of a linked list, determine if the linked list has a *cycle* in it.
```

Detect if the linked list has a cycle.

## What is a cycle(=loop)?

In the context of a linked list, a "cycle" or "loop" refers to a situation where the linked list contains a sequence of nodes that forms a closed loop, rather than a linear sequence where each node points to the next node in the list. This means that you can start at some node within the loop and follow the links, and you'll eventually reach the same node again by traversing the loop.

A linked list with a cycle is also known as a "circular linked list" or simply a "looped linked list."

## Approach

### DFS ( Dictionary; Hash Table )

Check a node had been visitied before.


```None
For every vertex v: visited(v) = finished(v) = false
For every vertex v: DFS(v)
```

- Time complexity : O(n)
- Space complexity : O(n)

### Floyd's cycle-finding algorithm(also known as the "tortoise and hare" algorithm)

This algorithm involves two pointers, one moving at a slower pace (tortoise) and the other at a faster pace (hare). If there's a cycle in the linked list, the two pointers will eventually meet at some node within the cycle.

- Time complexity :
  - When the linked list has no cycle: O(n)
    - In this case, the algorithm traverses the entire linked list once using both the slow and fast pointers. Since there is no cycle, the fast pointer will eventually reach the end of the list, indicating that there is no cycle. The algorithm runs in O(n) time, where "n" is the number of nodes in the linked list, because you visit each node once.
  - When the linked list has a cycle:
    - When there is a cycle in the linked list, the time complexity depends on the length of the cycle and the position of the pointers when they meet. Let's denote "k" as the number of nodes from the head of the list to the start of the cycle, and "m" as the number of nodes within the cycle.
    The slow pointer travels a distance of "k" before entering the cycle.
    The fast pointer travels a distance of "2k" (because it moves twice as fast) before entering the cycle.
    Once both pointers are in the cycle, they will meet after traveling a distance of "m - k" within the cycle.
    Therefore, the total number of steps or iterations required to detect the cycle is "k + (m - k) = m." This means that the time complexity in this case is O(m), where "m" is the length of the cycle.

  - When the linked list has a cycle, but the pointers meet at the start of the cycle:
    - In some cases, the pointers might meet at the start of the cycle, specifically when "k" is equal to zero. This means that the slow pointer and the fast pointer initially start at the same node. In this case, the algorithm will still detect the cycle correctly, but it will require one iteration to recognize the cycle. Therefore, the time complexity is still O(1).

- Space complexity : O(1)

    - The algorithm only uses two pointers (the tortoise and the hare) to traverse the linked list. These two pointers do not consume additional memory proportional to the size of the list.

