# 138. Copy List with Random Pointer

## Approach

### Iterate with O(N) Space

1. Create a mapping between the original nodes and their corresponding new nodes. This mapping will help you maintain the relationship between the original and copied nodes while creating the new linked list.
2. Traverse the original linked list and for each node, create a new node with the same value and append it to the new linked list. Also, update the mapping to associate the original node with the new node.
3. Traverse the original linked list again, and for each node, update the next and random pointers of the corresponding new node using the mapping you created in step 1.
4. Return the head of the new linked list.

### Without mapping

1. We create new nodes and insert them between the original nodes in a single pass. This way, we maintain the structure of the original linked list and its copied version side by side.
2. We then update the random pointers of the new nodes while iterating through the original list. When we encounter a node with a random pointer, we can easily access its corresponding new node, which is next to it.
3. Finally, we separate the original and copied linked lists by updating the next pointers of both lists. We restore the original list while keeping the copied list intact.
