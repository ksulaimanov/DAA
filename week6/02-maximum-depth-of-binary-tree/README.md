# Maximum Depth of Binary Tree

## 1. Problem

I get the root of a binary tree and must return its depth: the number of nodes on the longest path from the root down to a leaf. An empty tree has depth 0.

## 2. Approach

I used depth-first search with an explicit stack that stores pairs `(node, depth)`:

1. Push `(root, 1)`.
2. Pop a pair, update `best = max(best, depth)`.
3. Push the left and the right child with `depth + 1`.
4. When the stack is empty, `best` is the answer.

### Tracing for `[3, 9, 20, null, null, 15, 7]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [3, 9, 20, None, None, 15, 7]
pop  3 at depth 1   best=1
     push  9 with depth 2
     push 20 with depth 2
pop 20 at depth 2   best=2
     push 15 with depth 3
     push  7 with depth 3
pop  7 at depth 3   best=3
pop 15 at depth 3   best=3
pop  9 at depth 2   best=3
result: 3
```

How to read it: the tree has three levels (3 / 9, 20 / 15, 7). The stack goes into 20 first (it was pushed last), reaches 15 and 7 at depth 3, and then comes back to 9 at depth 2. The biggest depth seen is 3.

### Challenges and approaches I considered

**Recursion.** The first solution that comes to mind is `1 + max(depth(left), depth(right))`. It is correct for small trees, but Python's default recursion limit is 1000 calls, and the problem allows trees with about 10,000 nodes, so a chain-like tree can break it. `pitfall.py` builds a chain of 5,000 nodes:

```
tree: a chain of 5000 nodes
recursive: RecursionError: maximum recursion depth exceeded
iterative: 5000
```

The explicit stack keeps the same idea but stores the depth next to each node and does not use the call stack, so the long chain is not a problem.

**BFS.** Counting the levels with a queue also works. I preferred DFS with a stack because a queue can hold a whole level, which is much bigger than one path for wide trees.

## 3. Time Complexity

**O(n)**

Every node is pushed once and popped once, and each step costs O(1).

## Space Complexity

**O(h), where h is the height of the tree**

The stack contains the current path and at most one waiting sibling per level, so about h entries: O(n) for a chain, O(log n) for a balanced tree.

## 4. Reflection / Improvement

- O(n) time cannot be improved: any node could be the deepest one, so every node has to be looked at.
- A BFS needs O(w) memory (the widest level), which is worse for wide trees. With Morris-like threading the extra memory could go down to O(1), but the tree would be changed temporarily.

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
