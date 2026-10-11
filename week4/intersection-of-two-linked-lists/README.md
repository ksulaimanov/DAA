# Intersection of Two Linked Lists

## Problem
We have two linked lists. At some node they can join and then they share the same nodes until the end (like the letter Y). We need to return the node where they meet, or `null` if they never meet. "The same node" means the same object in memory, not just the same value.

## Approach
I wrote two versions.

**Version 1: brute force (my first solution).**
For every node of list A I walk through all nodes of list B and compare the nodes with `==`. The first pair where `a == b` is the intersection. If nothing is found, I return `null`.

**Version 2: two pointers.**
1. Put pointer `a` at the head of A and pointer `b` at the head of B.
2. In every iteration move both pointers one step.
3. When a pointer becomes `null` (the end of its list), move it to the head of the other list.
4. Stop when `a == b`. This is the intersection node, or `null` if both pointers reached the end at the same time (no intersection).

Why it works: pointer `a` walks list A and then list B, pointer `b` walks list B and then list A. Both pointers walk the same total length, so the different lengths of the lists do not matter. After the switch they arrive at the shared part at the same moment.

### Tracing (version 2), lists with intersection
A = `4 -> 1 -> 8 -> 4 -> 5`, B = `5 -> 6 -> 1 -> 8 -> 4 -> 5`. The nodes `8 -> 4 -> 5` are shared. The two `1` nodes are different nodes with the same value.

| Step | a | b |
|------|---|---|
| start | 4 (A) | 5 (B) |
| 1 | 1 (A) | 6 (B) |
| 2 | 8 | 1 (B) |
| 3 | 4 | 8 |
| 4 | 5 | 4 |
| 5 | null | 5 |
| 6 | 5 (head of B) | null |
| 7 | 6 (B) | 4 (head of A) |
| 8 | 1 (B) | 1 (A) |
| 9 | 8 | 8 |

At step 9 `a == b`, both point to the same node with value 8, so I return it. At step 8 both pointers show value 1, but these are different nodes, so the loop continues.

### Tracing (version 2), no intersection
A = `2 -> 6 -> 4`, B = `1 -> 5`.
`a` goes: 2, 6, 4, null, 1, 5, null.
`b` goes: 1, 5, null, 2, 6, 4, null.
After 6 steps both are `null`, so `a == b` and I return `null`.

## Challenges
- In the brute force I first compared values (`a.val == b.val`, method `getIntersectionNodeWrong`). For the example above it returned 4 instead of 8, because the first node of A has the value 4, and B also has a node with the value 4. Values can repeat in different nodes, so I must compare the nodes themselves with `==`.
- I also noticed that if I switch a pointer when `a.next == null` (and not when `a == null`), then in the "no intersection" case the pointers never become `null` together and the loop never stops. The `null` itself must be a step.

## Time Complexity
Let m be the length of A and n the length of B.
- Version 1: **O(m * n)**. For each of m nodes of A, the inner loop can walk all n nodes of B.
- Version 2: **O(m + n)**. Each pointer walks list A and list B at most one time, so there are about m + n iterations.

## Space Complexity
**O(1)** for both versions. I use only a few pointers.

## Reflection / Improvement
A middle solution is to put all nodes of A into a `HashSet` and then walk B and check if a node is in the set. It is O(m + n) time, but it needs O(m) extra memory. The two pointers version keeps the O(m + n) time and reduces the memory to O(1), so it is the best I know.
