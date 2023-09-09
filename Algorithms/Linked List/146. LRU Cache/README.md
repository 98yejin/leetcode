# 146. LRU Cache

## Problem

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Constraints

- 1 <= capacity <= 3000
- 0 <= key <= 104
- 0 <= value <= 105

### Hashmap and Doubly Linked list

![image](/Algorithms/Linked%20List/146.%20LRU%20Cache/images/146-1.jpg)

```python3
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
```

### Doubly linked list

A doubly linked list is a type of linked list in which each node contains pointers to both the previous node and the next node.

#### Why do we use doubly linked list?

- Efficient Removal and Insertion:

```None
With a doubly linked list, you can efficiently remove and insert elements at both ends (head and tail) in O(1) time complexity.
This is essential for LRU caching because when an item is accessed (used), it needs to be moved to the front (most recently used) of the list, and when the cache reaches its capacity and needs to evict the least recently used item, it should remove the element from the end (least recently used) of the list.
Doubly linked lists make these operations fast and straightforward.
```

- Maintaining LRU Order:

```None
The LRU order of elements is critical in an LRU cache. 
When an item is accessed (read or written), it becomes the most recently used item and should be moved to the front of the list. 
This can be done efficiently in O(1) time by simply removing the item from its current position and inserting it at the front of the list.
```

- Easy Removal of LRU Element:

```None
When the cache is full and needs to evict an item, it should remove the item from the end of the list (least recently used). 
A doubly linked list makes this operation efficient by allowing you to easily remove the tail element in O(1) time.
```

- Constant Time Access:

```None
Although access time in a doubly linked list is not O(1) like an array or hash table, it's still relatively fast, especially for reasonably sized caches.
When you need to check if an item is in the cache, you can traverse the list in O(n) time, but you can optimize this by maintaining a hash table or dictionary that maps keys to the corresponding nodes in the linked list, allowing for O(1) access time.
While a doubly linked list is a suitable data structure for implementing an LRU cache, it's essential to note that combining it with a hash table or dictionary for fast key-based access is a common practice to achieve the overall efficiency needed for an LRU cache.
This combination allows you to efficiently perform cache operations like inserting, accessing, and evicting items while preserving the LRU order.
```

### collections.OrderedDict

> Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.

OrderedDict is designed to maintain the order of elements based on the order in which they were added or accessed.
This makes it well-suited for building an LRU cache for several reasons:

- Ordered Structure:
  - OrderedDict is a built-in Python data structure that maintains the order of key-value pairs. When you insert elements into an OrderedDict, they are stored in the order they were added. This order can be leveraged to implement LRU behavior, where the most recently accessed or added items are at the front of the dictionary.
- Easy Removal of LRU Element:
  - Since OrderedDict maintains the order of elements, removing the least recently used item (which is at the end of the ordered dictionary) is a simple operation. This is crucial for maintaining the LRU cache policy.

> The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

- Simple Implementation:
  - Using OrderedDict simplifies the implementation of an LRU cache compared to manually managing a doubly linked list and a hash table. You don't need to handle low-level details like updating pointers or tracking the order of elements; OrderedDict takes care of this for you.

> The move_to_end() method moves an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist: