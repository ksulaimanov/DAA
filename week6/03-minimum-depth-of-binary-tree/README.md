# Minimum Depth of Binary Tree

## 1. Problem

I get the root of a binary tree and must return the number of nodes on the shortest path from the root to a leaf. A leaf is a node without any children, so a node with only one child is not a leaf.

## 2. Approach

I used breadth-first search with a queue of pairs `(node, depth)`:

1. Put `(root, 1)` in the queue.
2. Take the first pair. If the node has no children, it is a leaf and its depth is the answer.
3. Otherwise put its children in the queue with `depth + 1`.

BFS visits the tree level by level, so the first leaf that I meet is the closest one to the root.

### Tracing for `[3, 9, 20, null, null, 15, 7]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [3, 9, 20, None, None, 15, 7]
pop  3 at depth 1: not a leaf, push its children
     queue=[(9, 2), (20, 2)]
pop  9 at depth 2: it is a leaf -> answer 2
result: 2
```

How to read it: node 3 is not a leaf, so 9 and 20 go to the queue. Node 9 is taken next, it has no children, so the answer is its depth, 2. Nodes 20, 15 and 7 are never looked at.

### Challenges and approaches I considered

**Copying the maximum depth idea.** `1 + min(depth(left), depth(right))` looks natural, but a missing child counts as depth 0, so a node with only one child seems to end there although it is not a leaf. `pitfall.py` shows it on a chain:

```
tree: [2, None, 3, None, 4, None, 5, None, 6]
1 + min(left, right): 1
BFS (my solution)   : 5
```

A correct DFS needs a special case (if one child is missing, use the depth of the other child). BFS does not need any special case, and it can stop as soon as it finds the first leaf, so I chose BFS.

## 3. Time Complexity

**O(n)**

In the worst case (for example, all leaves are on the last level, or the tree is a chain) every node is processed once: O(n). Each node costs O(1). Often BFS stops much earlier, when a shallow leaf exists.

## Space Complexity

**O(w), where w is the maximum number of nodes on one level**

The queue holds at most about two levels of the tree. For a complete tree this is about n/2 nodes, so O(n) in the worst case; for a chain it is O(1).

## 4. Reflection / Improvement

- The worst case O(n) cannot be improved: the only shallow leaf can be anywhere, so in the worst case every node has to be checked.
- DFS needs only O(h) memory, which is better for wide trees. Its disadvantage is that it cannot stop at the first leaf (it has to compare all branches), so it often does more work than BFS.

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
