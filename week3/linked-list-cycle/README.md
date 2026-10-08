# Linked List Cycle

## Problem
We have a linked list. Sometimes the `next` pointer of the last node does not go to `null`, but goes back to one of the earlier nodes. Then the list has a cycle and we can walk in it forever. We need to return `true` if the list has a cycle and `false` if it does not.

## Approach
I wrote two versions.

**Version 1: HashSet (my first solution).**
I walk through the list and save every visited node in a `HashSet`. If I come to a node that is already in the set, I have been here before, so there is a cycle. If I reach `null`, there is no cycle. I store the nodes themselves (references), not their values, because different nodes can have the same value.

**Version 2: slow and fast pointers.**
I use two pointers that start at `head`. `slow` moves 1 step and `fast` moves 2 steps each iteration.
- If there is no cycle, `fast` reaches `null` and I return `false`.
- If there is a cycle, both pointers get inside it. Then `fast` is catching up with `slow` like a faster runner on a circle track, and they must meet in the same node, so I return `true`.

### Tracing (version 1)
Example: `3 -> 2 -> 0 -> -4`, and the last node (-4) points back to the node with value 2.

| Step | current node | visited set before check | In the set? |
|------|--------------|--------------------------|-------------|
| 1 | 3 | {} | no, add it |
| 2 | 2 | {3} | no, add it |
| 3 | 0 | {3, 2} | no, add it |
| 4 | -4 | {3, 2, 0} | no, add it |
| 5 | 2 (back again) | {3, 2, 0, -4} | yes, return true |

### Tracing (version 2) with a cycle
Same list. Start: `slow = 3`, `fast = 3`.

| Iteration | slow | fast | slow == fast? |
|-----------|------|------|---------------|
| 1 | 2 | 0 | no |
| 2 | 0 | 2 | no |
| 3 | -4 | -4 | yes, return true |

### Tracing (version 2) without a cycle
Example: `1 -> 2 -> 3 -> null`. Start: `slow = 1`, `fast = 1`.

| Iteration | slow | fast | slow == fast? |
|-----------|------|------|---------------|
| 1 | 2 | 3 | no |
| 2 | stop | fast = 3 and fast.next is null, so the loop ends | return false |

Edge cases: an empty list (`head == null`) and a one-node list without a cycle both give `false`, because the loop does not start.

## Time Complexity
**O(n)** for both versions, where n is the number of nodes.
- Version 1: each node is visited at most once. `contains` and `add` of a `HashSet` take O(1) on average, so the total is O(n).
- Version 2: without a cycle, `fast` reaches the end after about n / 2 iterations. With a cycle, after `slow` enters the cycle, the distance between `fast` and `slow` becomes smaller by 1 every iteration, so they meet in at most one cycle length more steps. In total it is not more than about n iterations.

## Space Complexity
- Version 1: **O(n)**. In the worst case (no cycle) the `HashSet` stores all n nodes.
- Version 2: **O(1)**. I use only two pointers, `slow` and `fast`, no matter how long the list is.

## Reflection / Improvement
The time is O(n) in both versions, but the HashSet version needs O(n) extra memory. The slow and fast pointers version removes this memory and uses O(1) space. It works because two pointers with different speeds must meet inside a cycle, so I do not need to remember the visited nodes.
