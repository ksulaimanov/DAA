# Path Sum

## 1. Problem

I get the root of a binary tree and a number `targetSum`. I must say whether there is a path from the root to a leaf whose values add up to `targetSum`.

## 2. Approach

I used depth-first search with an explicit stack of pairs `(node, remaining)`, where `remaining` is how much is still needed before this node:

1. Push `(root, targetSum)`.
2. Pop a pair and subtract the node's value: `remaining -= node.val`.
3. If the node is a leaf and `remaining == 0`, a path is found: return `True`.
4. Otherwise push the children with the new `remaining`.
5. If the stack becomes empty, return `False`.

Subtracting while going down means that I do not need to store the whole path.

### Tracing for `[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1] with target 22`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]  target: 22
pop  5: remaining after it =  17   leaf=False
pop  4: remaining after it =  13   leaf=False
pop 11: remaining after it =   2   leaf=False
pop  7: remaining after it =  -5   leaf=True
pop  2: remaining after it =   0   leaf=True
     leaf and remaining == 0 -> True
result: True
```

How to read it: the stack goes down the left side: 5 (17 left), 4 (13 left), 11 (2 left). Leaf 7 gives -5, so it fails. Leaf 2 gives 0, so the path 5 -> 4 -> 11 -> 2 has the sum 22 and the answer is `True`.

### Challenges and approaches I considered

I tested two ideas that look right but are wrong (`pitfall.py`):

```
tree [1, 2], target 1 (root is not a leaf, so the answer is False)
  correct          : False
  check every node : True
tree [10, -5], target 5 (10 + -5 = 5, so the answer is True)
  correct          : True
  prune if sum > target: False
```

**Checking every node.** If I compare the running sum with the target at every node, then `[1, 2]` with target 1 gives `True`, because the root alone has the sum 1. But the path must end at a leaf.

**Stopping a branch when the sum is already too big.** It looks like a free speed-up, but values can be negative: in `[10, -5]` the sum is 10 > 5 at the root, and the leaf brings it back to 5. So I cannot cut branches early.

## 3. Time Complexity

**O(n)**

In the worst case (no path matches) every node is popped once and costs O(1). If a matching path exists the search can stop earlier.

## Space Complexity

**O(h), where h is the height of the tree**

The stack holds the current path and one waiting sibling per level: O(n) for a chain, O(log n) for a balanced tree.

## 4. Reflection / Improvement

- O(n) is optimal in the worst case: when no path matches, every leaf has to be checked.
- If all values were non-negative, I could skip a branch as soon as the sum is bigger than the target. The worst case would still be O(n), but typical inputs would be faster.

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
