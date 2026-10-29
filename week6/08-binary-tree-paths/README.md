# Binary Tree Paths

## 1. Problem

I get the root of a binary tree and must return every path from the root to a leaf as a string like `"1->2->5"`.

## 2. Approach

I used depth-first search with one shared list `path`:

1. When I enter a node, I append its value to `path`.
2. If the node is a leaf, I join `path` with `"->"` and save the string.
3. Otherwise I go into the left child and then into the right child.
4. Before leaving the node I remove its value from `path` (**backtracking**), so `path` is again the way to the parent.

### Tracing for `[1, 2, 3, null, 5]`

The output below was produced by `trace.py` (it runs the same algorithm and prints every step):

```
tree: [1, 2, 3, None, 5]
enter 1   path=['1']
  enter 2   path=['1', '2']
    enter 5   path=['1', '2', '5']
      leaf -> save '1->2->5'
    leave 5   path=['1', '2']
  leave 2   path=['1']
  enter 3   path=['1', '3']
    leaf -> save '1->3'
  leave 3   path=['1']
leave 1   path=[]
result: ['1->2->5', '1->3']
```

How to read it: the search goes 1 -> 2 -> 5 and saves `1->2->5` at the leaf. On the way back each `leave` removes one value. Then it goes 1 -> 3 and saves `1->3`.

### Challenges and approaches I considered

**Forgetting to backtrack.** Without `path.pop()` the list keeps the values of the branches that are already finished (`pitfall.py`):

```
tree: [1, 2, 3, None, 5]
with path.pop()    : ['1->2->5', '1->3']
without path.pop() : ['1->2->5', '1->2->5->3']
```

**Passing a string instead of a list.** The path can also be passed as a string (`path + "->" + str(val)`). Then no `pop` is needed, because strings are not shared, but a new string is created at every node. I used a list and joined it only at leaves.

## 3. Time Complexity

**O(n * h), where h is the height of the tree**

The search visits every node once, O(n). At every leaf I build a string from a path of at most h values, which costs O(h). With L leaves the total is O(n + L * h), which is at most O(n * h). For a balanced tree this is O(n log n). The worst case is a "caterpillar" tree (a long chain where every chain node also has a leaf): about n/2 leaves with paths of length up to n/2, so O(n^2). The answer itself has this size, so it cannot be avoided.

## Space Complexity

**O(h) extra space**

The recursion stack and the `path` list both have at most h entries. The returned strings (up to O(L * h) characters) are the output and are not counted.

## 4. Reflection / Improvement

- The running time is proportional to the total length of the output strings, so I think this is the best possible.
- If recursion depth were a problem, the same search can be done with an explicit stack that stores `(node, path_string)`.

## Files

- `solution.py`: the solution with a self-test (`python3 solution.py`); it compares my result with a simple recursive reference on 500 random trees
- `trace.py`: prints the tracing above
- `pitfall.py`: the wrong versions described in the challenges section
- `tree_utils.py`: helpers that build a tree from LeetCode's list format and print it back
