# Binary Tree Preorder Traversal

## 1. Problem

I get the root of a binary tree and must return its values in preorder order: the node first, then the whole left subtree, then the whole right subtree.

## 2. Approach

I used an explicit stack:

1. Push the root.
2. Pop a node and visit it (append its value).
3. Push its right child first and then its left child, so the left child is popped next.
4. Repeat until the stack is empty.

### Tracing for `[1, null, 2, 3]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [1, None, 2, 3]
pop  1 -> visit   result=[1]
     push right 2
     stack=[2]
pop  2 -> visit   result=[1, 2]
     push left  3
     stack=[3]
pop  3 -> visit   result=[1, 2, 3]
     stack=[]
result: [1, 2, 3]
```

How to read it: 1 is visited, and its only child 2 is pushed. Then 2 is visited and its left child 3 is pushed. Then 3 is visited. The visit order is 1, 2, 3.

### Challenges and approaches I considered

**Recursion.** The recursive version (node, left, right) is simple. I used the stack to avoid the call stack (the follow-up asks for an iterative solution) and kept the recursive version only as a reference in the self-test.

**Order of pushing.** A stack gives back the last element first. If I push the left child before the right child, the right child comes out first and the order of siblings is wrong (`pitfall.py`):

```
tree: [1, 2, 3]
push right, then left : [1, 2, 3]
push left, then right : [1, 3, 2]
```

So the right child has to be pushed first.

## 3. Time Complexity

**O(n)**

Every node is pushed once and popped once, each step costs O(1).

## Space Complexity

**O(h), where h is the height of the tree**

The stack holds the waiting right siblings along the current path: O(n) for a chain, O(log n) for a balanced tree. The result list is the required output and is not counted.

## 4. Reflection / Improvement

- O(n) time is optimal.
- **Morris preorder** reaches O(1) extra space: for a node with a left subtree, the rightmost node of that subtree is temporarily linked back to the node, and the link is removed on the second visit. I would replace the stack with these temporary links. Time stays O(n).

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
