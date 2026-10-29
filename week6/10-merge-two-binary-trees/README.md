# Merge Two Binary Trees

## 1. Problem

I get two binary trees and must lay one over the other. If both trees have a node at the same position, the new value is the sum. If only one of them has a node there, that node is used as it is.

## 2. Approach

I merge the second tree into the first one, in place, with a stack of pairs of nodes that exist in both trees:

1. If one root is empty, return the other root.
2. Push `(root1, root2)`.
3. Pop a pair `(a, b)` and do `a.val += b.val`.
4. For each side (left, right):
   - both have a child: push that pair of children;
   - only `b` has a child: attach the whole subtree of `b` to `a`, no need to look inside;
   - only `a` has a child: nothing to do.
5. Return `root1`.

### Tracing for `[1, 3, 2, 5] and [2, 1, 3, null, 4, null, 7]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree 1: [1, 3, 2, 5]
tree 2: [2, 1, 3, None, 4, None, 7]
pair a=1, b=2: a.val becomes 3
   left : both have a child -> push pair (3, 1)
   right: both have a child -> push pair (2, 3)
pair a=2, b=3: a.val becomes 5
   left : no children
   right: only b has 7 -> attach b's subtree to a
pair a=3, b=1: a.val becomes 4
   left : only a has 5 -> keep it
   right: only b has 4 -> attach b's subtree to a
result: [3, 4, 5, 5, 4, None, 7]
```

How to read it: the roots 1 and 2 become 3. Both have a left and a right child, so two pairs are pushed. Pair (2, 3) becomes 5, only tree 2 has a right child 7, so it is attached. Pair (3, 1) becomes 4, tree 1 keeps its child 5, and tree 2's child 4 is attached on the right. The result is `[3, 4, 5, 5, 4, null, 7]`.

### Challenges and approaches I considered

**Returning `None` when one side is empty.** If I write `if a is None or b is None: return None`, the subtrees that exist in only one tree are lost (`pitfall.py`):

```
tree 1: [1, 3, 2, 5]
tree 2: [2, 1, 3, None, 4, None, 7]
mine                            : [3, 4, 5, 5, 4, None, 7]
return None if one side is empty: [3, 4, 5]
```

The right rule is to return the **other** node, because it is already the correct result for that position.

**Recursion.** The recursive version (`if not a: return b`, `if not b: return a`, ...) is shorter. The problem allows trees with up to 2,000 nodes, which can be deeper than Python's default recursion limit of 1000, so I used a stack.

## 3. Time Complexity

**O(min(n, m)), where n and m are the sizes of the trees**

Each loop iteration handles one position where both trees have a node, and costs O(1). A subtree that exists in only one tree is attached or kept in O(1) without visiting it. So the number of iterations is at most the number of overlapping positions, which is at most min(n, m).

## Space Complexity

**O(min(h1, h2)) in the best case, O(min(n, m)) in the worst case**

The stack contains pairs along one path of the overlapping part, so at most min(h1, h2) pairs, where h1 and h2 are the heights. No new nodes are created.

## 4. Reflection / Improvement

- The merged tree shares nodes with the input trees and changes the first tree. If the result must be independent, I would create a new node for every position, which costs O(n + m) time and memory.
- Time O(min(n, m)) is already very good: only the overlapping part is visited.

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
