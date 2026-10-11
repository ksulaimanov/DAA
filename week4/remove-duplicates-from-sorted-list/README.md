# Remove Duplicates from Sorted List

## Problem
We have a sorted linked list. Some values appear more than once. We need to delete the extra nodes so that every value stays only one time, and return the list. The list must stay sorted.

## Approach
I wrote two versions.

**Version 1: brute force (my first solution).**
For every node `cur` I start a second pointer `runner` and walk to the end of the list. Every node after `cur` with the same value is deleted (`runner.next = runner.next.next`). Then I move `cur` to the next node. This does not use the fact that the list is sorted.

**Version 2: one pass.**
Because the list is sorted, equal values are always neighbors. So I only compare `cur` with `cur.next`:
1. If `cur.val == cur.next.val`, delete the next node (`cur.next = cur.next.next`) and stay on the same `cur`.
2. Otherwise move `cur` forward.
3. Stop when `cur` or `cur.next` is `null`.

### Tracing (version 2)
Example: `1 -> 1 -> 2 -> 3 -> 3`

| Step | cur | cur.next | Equal? | Action | List after the step |
|------|-----|----------|--------|--------|---------------------|
| 1 | 1 | 1 | yes | delete next node | 1 -> 2 -> 3 -> 3 |
| 2 | 1 | 2 | no | move cur | 1 -> 2 -> 3 -> 3 |
| 3 | 2 | 3 | no | move cur | 1 -> 2 -> 3 -> 3 |
| 4 | 3 | 3 | yes | delete next node | 1 -> 2 -> 3 |
| 5 | 3 | null | - | stop | 1 -> 2 -> 3 |

### Tracing (version 1)
Same example. `cur` = first 1: `runner` walks the list and deletes the second 1. `cur` = 2: `runner` walks and finds nothing. `cur` = 3: `runner` deletes the second 3. Result: `1 -> 2 -> 3`.

## Challenges
- My first idea was the brute force with two loops, because I did not think about the sorted order. It gives the right answer (it even works on an unsorted list), but for every node it walks through the whole rest of the list, so it is slow.
- In the one-pass version I tried to move `cur` forward after every step, also after deleting a node. For `1 -> 1 -> 1 -> 2` I got `1 -> 1 -> 2` (method `deleteDuplicatesWrong` in the code). After deleting the second 1, `cur` jumped to the third 1 and never compared it with the first 1. The fix is to move `cur` only when the next value is different.

## Time Complexity
- Version 1: **O(n²)**. For every node the `runner` can walk through the rest of the list. In the worst case (all values are different) it is (n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2 steps.
- Version 2: **O(n)**. Every iteration either deletes one node or moves `cur` forward, so there are at most n iterations.

## Space Complexity
**O(1)** for both versions. I only use the pointers `cur` and `runner` and I change the existing links, without new nodes.

## Reflection / Improvement
The brute force does not use that the list is sorted. In a sorted list the duplicates stand next to each other, so one pass is enough: time goes from O(n²) to O(n), space stays O(1). It can not be faster than O(n), because we have to look at every node at least once.
