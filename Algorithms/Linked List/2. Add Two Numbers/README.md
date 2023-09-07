# 2. Add Two Numbers

## Problem

```None
Add the two numbers and return the sum as a linked list.

- linked lists are non-empty and each node contains a single digit
- digits stored in reverse order
```

## Approach

## Convert the linked list into integers

- converts linked lists into integers
- compute their sum
- converts the sum back into a linked list

## Without converting the linked list into integers

We simplify above appoach by directly building the result linked list instead of converting to an integer and then back to a linked list.

- iterate through both linked list
  - adding corresponding digits along with the crarry from the previous iteration
  - create a new node with the result digit and update the carry for the next iteration
