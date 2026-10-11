# Remove Linked List Elements

## Problem
We have a linked list and a number `val`. We need to delete all nodes whose value is equal to `val` and return the new head of the list. The head itself can also be deleted.

## Approach
I wrote two versions.

**Version 1: brute force (my first solution).**
I walk through the list and put every value that is not equal to `val` into an `ArrayList`. Then I build a completely new list from this `ArrayList`.

**Version 2: in place with a dummy node.**
1. Create a `dummy` node and set `dummy.next = head`. Now the first node also has a node before it.
2. Set `cur = dummy`.
3. While `cur.next != null`: if `cur.next.val == val`, delete it with `cur.next = cur.next.next` and do NOT move `cur` (the new next node must be checked too). Otherwise move `cur` forward.
4. Return `dummy.next`.

### Tracing (version 2)
Example: `1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6`, `val = 6`

| Step | cur | cur.next | next == 6? | Action | List after the step |
|------|-----|----------|------------|--------|---------------------|
| 1 | dummy | 1 | no | move cur | 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 |
| 2 | 1 | 2 | no | move cur | 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 |
| 3 | 2 | 6 | yes | delete next node | 1 -> 2 -> 3 -> 4 -> 5 -> 6 |
| 4 | 2 | 3 | no | move cur | 1 -> 2 -> 3 -> 4 -> 5 -> 6 |
| 5 | 3 | 4 | no | move cur | 1 -> 2 -> 3 -> 4 -> 5 -> 6 |
| 6 | 4 | 5 | no | move cur | 1 -> 2 -> 3 -> 4 -> 5 -> 6 |
| 7 | 5 | 6 | yes | delete next node | 1 -> 2 -> 3 -> 4 -> 5 |
| 8 | 5 | null | - | stop | 1 -> 2 -> 3 -> 4 -> 5 |

### Tracing (version 1)
Same example: kept values `[1, 2, 3, 4, 5]`, then a new list `1 -> 2 -> 3 -> 4 -> 5` is built.

## Challenges
- My first in-place solution had no dummy node: I checked only `cur.next` starting from `head` (method `removeElementsWrong`). For `6 -> 1 -> 6 -> 2` and `val = 6` it returned `6 -> 1 -> 2`, because nobody checks the head itself. The dummy node solves this: the head becomes a normal "next" node.
- I also noticed that if I move `cur` forward after deleting a node, I skip the next node. For example, with two 6 in a row, the second 6 would stay in the list. So after a deletion `cur` stays where it is.

## Time Complexity
**O(n)** for both versions. In version 1 I walk the list once and then walk the `ArrayList` once. In version 2 every iteration either deletes a node or moves `cur`, so there are at most n iterations.

## Space Complexity
- Version 1: **O(n)**. The `ArrayList` and the new nodes can contain up to n elements.
- Version 2: **O(1)**. Only the `dummy` node and the `cur` pointer are used, and I change the existing links.

## Reflection / Improvement
The time is O(n) in both versions and it can not be better, because every node must be checked. The improvement is in memory: the dummy node version works in place and uses O(1) extra space instead of O(n). There is also a recursive solution (remove the matching nodes after the head, then check the head), but it uses O(n) memory for the call stack, so it is not better in space.
