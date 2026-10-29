# Sum of Left Leaves

## 1. Problem

I get the root of a binary tree and must return the sum of all leaves that are the left child of their parent. A leaf is a node without children.

## 2. Approach

A leaf cannot know whether it is a left or a right child, so I check from the parent's side:

1. Use a stack and start with the root.
2. Pop a node. If its left child exists and has no children itself, add the left child's value to `total`.
3. Push the node's children on the stack.
4. When the stack is empty, return `total`.

Checking from the parent also solves the special case of a single node: the root has no parent, so it is never counted.

### Tracing for `[3, 9, 20, null, null, 15, 7]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [3, 9, 20, None, None, 15, 7]
node  3: left child 9 is a leaf -> total=9
node 20: left child 15 is a leaf -> total=24
node  7: left child is None (not a left leaf) -> total=24
node 15: left child is None (not a left leaf) -> total=24
node  9: left child is None (not a left leaf) -> total=24
result: 24
```

How to read it: node 3 has the left child 9, which is a leaf, so total becomes 9. Node 20 has the left child 15, which is a leaf, so total becomes 24. Nodes 7, 15 and 9 have no left child. The answer is 24 (9 + 15).

### Challenges and approaches I considered

**Counting too much.** Two wrong versions I tested (`pitfall.py`):

```
tree: [1, 2, 3, 4, 5] (the only left leaf is 4)
correct                  : 4
sum of all left children : 6
sum of all leaves        : 12
```

Adding every left child is wrong because a left child can have its own children (node 2 here). Adding every leaf is wrong because right leaves (5 and 3) are not allowed. A node counts only if it is a **left child and a leaf at the same time**.

## 3. Time Complexity

**O(n)**

Every node is pushed and popped once, and the leaf check costs O(1).

## Space Complexity

**O(h), where h is the height of the tree**

The stack holds the current path and waiting siblings: O(n) for a chain, O(log n) for a balanced tree.

## 4. Reflection / Improvement

- O(n) time is optimal, every node has to be looked at.
- Memory could go down to O(1) with Morris traversal, at the price of temporarily changing the tree.

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
