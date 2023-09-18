# 27. Remove Element

## in-place algorithm

Algorithm that operrates directly on the input data structure without requiring extra space proportinal to the input size.
That is to say, it modifies the input in place, without creating a seperate copy of the data structure.

```none
in-place <-> (not-in-place or out-of-place)

```

### in it's strictest form

The algorithm can only have a constant amount of extra space, counting evertything inluding function calls and pointers.
however, this form is very limited as simply having an index to a length n array requires O(log n)bits.

### more broadly

The algorithm does not use extra space for manipluating the input but may require a small though nonconstant extra space for its pperating. Usually, this pace is O(log n), though sometimes anything in O(n) is allowed. Note that space complexity also varied choices in whether of not to count the index lenghts as part of the space used. Often, the space complexity is given in terms of the number of indices or pointers needed, ignoring their length.
