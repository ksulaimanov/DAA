# Binary Tree Inorder Traversal

## 1. Problem

I get the root of a binary tree and must return its values in inorder order: first the whole left subtree, then the node itself, then the whole right subtree.

## 2. Approach

I used an explicit stack instead of recursion (the follow-up of the problem asks for an iterative solution):

1. `curr` starts at the root.
2. Go left as far as possible and push every node on the stack. These nodes are waiting until their left subtree is finished.
3. Pop a node. Its left subtree is completely done, so I visit it (append its value).
4. Move to its right child and repeat from step 2.
5. Stop when `curr` is empty and the stack is empty.

### Tracing for `[1, null, 2, 3]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [1, None, 2, 3]
push  1  (go left)   stack=[1]
pop   1  (visit)     stack=[]  result=[1]
     go right -> 2
push  2  (go left)   stack=[2]
push  3  (go left)   stack=[2, 3]
pop   3  (visit)     stack=[2]  result=[1, 3]
     go right -> None
pop   2  (visit)     stack=[]  result=[1, 3, 2]
     go right -> None
result: [1, 3, 2]
```

How to read it: node 1 has no left child, so it is visited at once (`[1]`) and we go right to node 2. Node 2 has a left child 3, so 2 waits on the stack while 3 is visited (`[1, 3]`). Only after that 2 is popped and visited (`[1, 3, 2]`). The stack is empty and there is nothing on the right, so the answer is `[1, 3, 2]`.

### Challenges and approaches I considered

**Recursion.** The shortest solution is recursive (left, visit, right). It is correct, but it relies on the call stack, and the follow-up asks for an iterative version. I used the recursive function only as a reference in the self-test.

**Forgetting to go right.** A bug I tested on purpose (`pitfall.py`): after visiting a node I set `curr = None` instead of `curr = curr.right`:

```
tree: [1, None, 2, 3]
correct           : [1, 3, 2]
forgot node.right : [1]
```

Nodes that are only reachable through a right child are never visited. The stack only remembers nodes that are waiting for their left subtree, so the right subtree has to be started explicitly after the visit.

## 3. Time Complexity

**O(n)**

Every node is pushed on the stack exactly once and popped exactly once. The inner `while` loops together make n pushes, the outer loop makes n pops, and each step costs O(1).

## Space Complexity

**O(h), where h is the height of the tree**

The stack holds the nodes on the current left spine: at most one path from the root down. That is O(n) for a tree that is a chain and O(log n) for a balanced tree. The result list (n values) is the required output, so I do not count it.

## 4. Reflection / Improvement

- O(n) time is optimal, every node has to be visited.
- Memory can be improved with **Morris traversal**: O(1) extra space. Before going into the left subtree, the rightmost node of that subtree is temporarily linked to the current node (a "thread"), so there is a way back without a stack. After coming back, the thread is removed and the tree is restored. I would replace the stack by these temporary links. Time stays O(n).

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
