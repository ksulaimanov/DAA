# Binary Tree Postorder Traversal

## 1. Problem

I get the root of a binary tree and must return its values in postorder order: the whole left subtree, then the whole right subtree, and the node itself last.

## 2. Approach

Postorder is the hardest of the three to do with a stack, because a node must wait for both subtrees. I used this observation:

> postorder (left, right, node) is the **reverse** of (node, right, left).

1. Run a preorder-like traversal with a stack, but push the left child first and the right child second, so the right child comes out first. This visits the nodes in the order node, right, left.
2. Reverse the list of visited values at the end.

### Tracing for `[1, null, 2, 3] and [1, 2, 3]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [1, None, 2, 3]
  visit 1   order=[1]   stack=[2]
  visit 2   order=[1, 2]   stack=[3]
  visit 3   order=[1, 2, 3]   stack=[]
  root-right-left order : [1, 2, 3]
  reversed = postorder  : [3, 2, 1]

tree: [1, 2, 3]
  visit 1   order=[1]   stack=[2, 3]
  visit 3   order=[1, 3]   stack=[2]
  visit 2   order=[1, 3, 2]   stack=[]
  root-right-left order : [1, 3, 2]
  reversed = postorder  : [2, 3, 1]
```

How to read it: for `[1, 2, 3]` the traversal visits 1, then 3, then 2 (node, right, left). Reversed this is `[2, 3, 1]`: left, right, node, which is the postorder. For `[1, null, 2, 3]` the visit order is 1, 2, 3 and the reversed list is `[3, 2, 1]`.

### Challenges and approaches I considered

**Reversing the ordinary preorder.** My first thought was to reverse the normal preorder (node, left, right). But its reverse is (right, left, node), not (left, right, node). `pitfall.py` shows the difference:

```
tree: [1, 2, 3]
root-right-left, reversed (mine)      : [2, 3, 1]
ordinary preorder, reversed (wrong)   : [3, 2, 1]
```

The mirrored order (node, right, left) is the one whose reverse is the postorder.

**One stack with a "last visited" pointer.** It avoids the final reversal, but it needs more conditions (is the right child already done?). I chose the reverse trick because it is easier to prove and to check.

## 3. Time Complexity

**O(n)**

Every node is pushed and popped once (O(n)), and the final reversal of n values is O(n) too.

## Space Complexity

**O(h), where h is the height of the tree**

The stack holds the current path and waiting siblings, about h nodes. The result list has n values (it is the required output).

## 4. Reflection / Improvement

- O(n) time is optimal.
- The reversal can be avoided with the one-stack version that remembers the last visited node.
- Morris postorder uses O(1) extra space, but it is much harder: it has to reverse the right edge of the tree on the way. Time stays O(n).

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
