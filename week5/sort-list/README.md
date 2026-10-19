# Sort List

## 1. Problem

I get the head of a singly linked list and must return the list sorted in ascending order. The follow-up asks for O(n log n) time and as little memory as possible. A linked list has no indexes, so I cannot jump to the middle or swap elements by position.

## 2. Approach

I used **merge sort on the list itself**:

1. **Base case.** An empty list or a list with one node is already sorted.
2. **Split.** Find the middle with two pointers: `slow` moves 1 node per step, `fast` moves 2 nodes. When `fast` reaches the end, `slow` is at the end of the first half. Then I cut the list: `second = slow.next; slow.next = None`.
3. **Sort** both halves recursively.
4. **Merge.** A dummy head and a `tail` pointer: compare the first nodes of both lists, link the smaller one after `tail`, move forward. When one list ends, link the rest of the other. No new nodes are created, only `next` pointers change.

### Tracing for `4 -> 2 -> 1 -> 3`

Finding the middle: `slow` = node 4, `fast` = node 2. `fast.next` exists (node 1), so `slow` moves to node 2 and `fast` moves to node 3. Now `fast.next` is `None`, the loop stops. `slow` is node 2, so the halves are `4 -> 2` and `1 -> 3`.

The output below was produced by `trace.py` (it prints every split, the node where `slow` stops, and every merge):

```
input: [4 -> 2 -> 1 -> 3]
split [4 -> 2 -> 1 -> 3]  (slow stops at 2) -> [4 -> 2] | [1 -> 3]
  split [4 -> 2]  (slow stops at 4) -> [4] | [2]
    base  [4]
    base  [2]
  merge [4] + [2] -> [2 -> 4]
  split [1 -> 3]  (slow stops at 1) -> [1] | [3]
    base  [1]
    base  [3]
  merge [1] + [3] -> [1 -> 3]
merge [2 -> 4] + [1 -> 3] -> [1 -> 2 -> 3 -> 4]
result: [1 -> 2 -> 3 -> 4]
```

How to read it: `4 -> 2` is split into `4` and `2` and merged into `2 -> 4`; `1 -> 3` is split and merged back into `1 -> 3`. The last merge of `2 -> 4` and `1 -> 3`: compare 2 and 1, take 1; compare 2 and 3, take 2; compare 4 and 3, take 3; the first list still has 4, so link it. Result: `1 -> 2 -> 3 -> 4`.

### Challenges and approaches I considered

**Copy values into an array.** Copy all values into a Python list, sort it, write the values back into the nodes. It is correct and short, but it needs O(n) extra memory and does not use the structure of the list, so I did not use it as the main solution.

**Finding the middle by counting.** I could walk the list once to count the nodes, then walk n/2 steps. It works, but it needs an extra pass. The slow/fast pointers find the middle in one pass.

**Forgetting to cut the list.** If I find the middle but do not set `slow.next = None`, the "first half" still contains all the nodes. For a list of two nodes the function calls itself with the same list again and never stops. I reproduced it in `pitfall.py`:

```
RecursionError: maximum recursion depth exceeded
```

## 3. Time Complexity

**O(n log n)**

Why: every call splits the list in half, so the recursion has about log₂ n levels. On one level, all the calls together walk the lists to find the middles (about n/2 steps in total) and merge them (about n steps in total), so one level costs O(n). In total O(n) × O(log n). As a formula: T(n) = 2·T(n/2) + O(n) = O(n log n).

## Space Complexity

**O(log n)**

Why: I do not create new nodes or arrays, the merge only relinks existing nodes. The only extra memory is the recursion stack, whose depth is about log₂ n. So it is not exactly O(1), because of the stack.

## 4. Reflection / Improvement

- Time cannot be better than O(n log n) for sorting by comparisons, but the memory can go down to **O(1)** with **bottom-up merge sort**.
- What to change: remove the recursion. First merge sublists of size 1 into sorted sublists of size 2, then merge sublists of size 2 into size 4, and so on, doubling the size until it is at least n. For this I need a helper that cuts a chunk of a given size from the list. Only a few pointers are used, so the extra space is O(1), and the time stays O(n log n).

## Files

- `solution.py`: the solution (with a small self-test, run `python3 solution.py`)
- `trace.py`: prints the tracing (`python3 trace.py 4 2 1 3`)
- `pitfall.py`: the "forgot to cut the list" bug
