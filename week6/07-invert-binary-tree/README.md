# Invert Binary Tree

## 1. Problem

I get the root of a binary tree and must mirror it: in every node the left and the right child swap places. The function returns the root of the mirrored tree.

## 2. Approach

I used recursion:

1. If the node is empty, return `None`.
2. Invert the right subtree and the left subtree (two recursive calls).
3. Assign the inverted right subtree to `left` and the inverted left subtree to `right`.

I do it in one statement: `root.left, root.right = invert(root.right), invert(root.left)`. Python evaluates the whole right side first, so the old children are not lost and no temporary variable is needed.

### Tracing for `[4, 2, 7, 1, 3, 6, 9]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [4, 2, 7, 1, 3, 6, 9]
invert(4)
  invert(7)
    invert(9)
    swap done at 9: left=None, right=None
    invert(6)
    swap done at 6: left=None, right=None
  swap done at 7: left=9, right=6
  invert(2)
    invert(3)
    swap done at 3: left=None, right=None
    invert(1)
    swap done at 1: left=None, right=None
  swap done at 2: left=3, right=1
swap done at 4: left=7, right=2
result: [4, 7, 2, 9, 6, 3, 1]
```

How to read it: the calls go to the leaves first. Leaves 9 and 6 have nothing to swap, then node 7 gets `left=9, right=6` (they were 6 and 9). The same happens for node 2 (`left=3, right=1`). Finally the root 4 gets `left=7, right=2`. The result is `[4, 7, 2, 9, 6, 3, 1]`.

### Challenges and approaches I considered

**Overwriting a child before using it.** Writing the swap as two separate statements is a bug (`pitfall.py`):

```
tree: [4, 2, 7, 1, 3, 6, 9]
correct                       : [4, 7, 2, 9, 6, 3, 1]
two separate assignments (bug): [4, 7, 7, 9, 9, 9, 9]
```

After `root.left = invert(root.right)` the old left child is gone, so the second line inverts the new `root.left` again. Both children end up pointing at the same subtree. The one-line assignment (or a temporary variable) avoids it.

**Iterative version.** A queue or a stack that swaps the two children of every node also works. For this problem the depth of the recursion is small (the tree is small), so I kept the simpler recursive version.

## 3. Time Complexity

**O(n)**

Every node is visited exactly once and the swap costs O(1).

## Space Complexity

**O(h), where h is the height of the tree**

The memory is the recursion stack: one call per level of the current path. It is O(log n) for a balanced tree and O(n) for a chain. No new nodes are created.

## 4. Reflection / Improvement

- O(n) time is optimal, every node has to be touched.
- An iterative version (stack or queue) removes the risk of a too deep recursion: it needs O(h) memory with a stack, or O(w) with a queue.

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
