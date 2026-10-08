# Merge Two Sorted Lists

## Problem
We have two linked lists, and each of them is already sorted in increasing order. We need to join them into one sorted linked list and return its head.

## Approach
I wrote two versions.

**Version 1: brute force (my first solution).**
1. Go through both lists and put all values into an `ArrayList`.
2. Sort the `ArrayList`.
3. Build a new linked list from the sorted values.

This works, but it does not use the fact that the lists are already sorted.

**Version 2: two pointers.**
I use a `dummy` node and a `tail` pointer. `list1` and `list2` point to the current nodes of the two lists.
1. While both lists are not finished, compare `list1.val` and `list2.val`.
2. Attach the smaller node to `tail.next` and move that list forward. Move `tail` forward too.
3. When one list is finished, attach the rest of the other list (it is already sorted).
4. Return `dummy.next`.

### Tracing (version 2)
Example: `list1 = 1 -> 2 -> 4`, `list2 = 1 -> 3 -> 4`

| Step | list1 points to | list2 points to | Compare | Action | Result so far |
|------|-----------------|-----------------|---------|--------|---------------|
| 1 | 1 | 1 | 1 <= 1 true | take from list1 | 1 |
| 2 | 2 | 1 | 2 <= 1 false | take from list2 | 1 -> 1 |
| 3 | 2 | 3 | 2 <= 3 true | take from list1 | 1 -> 1 -> 2 |
| 4 | 4 | 3 | 4 <= 3 false | take from list2 | 1 -> 1 -> 2 -> 3 |
| 5 | 4 | 4 | 4 <= 4 true | take from list1 | 1 -> 1 -> 2 -> 3 -> 4 |
| end | null | 4 | list1 is finished | attach the rest of list2 | 1 -> 1 -> 2 -> 3 -> 4 -> 4 |

Edge cases: if both lists are empty, the loop does not run and `dummy.next` is `null`. If one list is empty, the rest of the other list is attached at once.

### Tracing (version 1)
Same example: collected values `[1, 2, 4, 1, 3, 4]`, after sorting `[1, 1, 2, 3, 4, 4]`, then a new list `1 -> 1 -> 2 -> 3 -> 4 -> 4` is built.

## Time Complexity
Let n and m be the lengths of the lists, and k = n + m.
- Version 1: **O(k log k)**. Reading the lists and building the new list is O(k), but sorting k values costs O(k log k), and this is the biggest part.
- Version 2: **O(n + m)**. Every step of the loop moves one pointer forward and takes one node. Each node is taken exactly once, so there are at most n + m steps.

## Space Complexity
- Version 1: **O(n + m)**. I store all values in an `ArrayList` and create n + m new nodes.
- Version 2: **O(1)** extra space. I do not create new nodes (only one `dummy` node). I just change the `next` links of the existing nodes and use a few pointers.

## Reflection / Improvement
The brute-force version ignores that both lists are sorted, so it pays for sorting. The two-pointer version uses this fact and improves the time from O(k log k) to O(n + m) and the extra space from O(n + m) to O(1). It cannot be much better, because we must look at every node at least once. There is also a recursive version, but it uses O(n + m) call stack.
