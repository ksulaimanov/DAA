# Sort an Array

## 1. Problem

I get an array of integers and must return it sorted in ascending order. Built-in sort functions are not allowed, the time must be O(n log n), and the extra memory should be as small as possible. The array can have up to 50,000 elements, so an O(n²) algorithm is too slow.

## 2. Approach

I used **merge sort** (divide and conquer):

1. **Divide.** Split the range `[lo, hi]` in the middle: left half `lo..mid`, right half `mid+1..hi`.
2. **Conquer.** Sort both halves recursively. A range with 0 or 1 element is already sorted, this is the base case.
3. **Combine.** Merge the two sorted halves with two pointers: `i` goes over the left half, `j` over the right half. At every step the smaller of `a[i]` and `a[j]` is written to a buffer. When one half is finished, the rest of the other half is copied. Then the buffer is copied back into the array.

I create one buffer of size n at the start and reuse it in all merges, so I do not allocate new lists on every recursion level.

### Tracing for `[5, 2, 3, 1]`

The output below was produced by `trace.py` (it prints every split and merge):

```
input: [5, 2, 3, 1]
split [5, 2, 3, 1] -> [5, 2] | [3, 1]
  split [5, 2] -> [5] | [2]
    base  [5]
    base  [2]
  merge [5] + [2] -> [2, 5]
  split [3, 1] -> [3] | [1]
    base  [3]
    base  [1]
  merge [3] + [1] -> [1, 3]
merge [2, 5] + [1, 3] -> [1, 2, 3, 5]
result: [1, 2, 3, 5]
```

How to read it: the array is cut until single elements remain (base case). Then the merges go back up. `[5]` + `[2]` becomes `[2, 5]`, and `[3]` + `[1]` becomes `[1, 3]`. In the last merge of `[2, 5]` and `[1, 3]`: compare 2 and 1, take 1; compare 2 and 3, take 2; compare 5 and 3, take 3; the left half still has 5, so take 5. Result: `[1, 2, 3, 5]`.

### Challenges and approaches I considered

**Insertion sort (simple brute force).** It is easy to write and correct, but every element may be shifted past all the elements before it. I measured it against my merge sort with `brute_force_bench.py` on random arrays (table below, measured on my machine):

```
      n |  insertion sort | merge sort
   1000 |         0.038 s |   0.0037 s
   2000 |         0.163 s |   0.0072 s
   4000 |         0.662 s |   0.0160 s
   8000 |         2.590 s |   0.0334 s
  16000 |         8.059 s |   0.0471 s
```

When n doubles, insertion sort takes roughly 3-4 times longer (0.163 s, 0.662 s, 2.590 s), which is the sign of O(n²). Merge sort takes only about 1.5-2 times longer. Extrapolating the last row to n = 50,000 gives about 8 s × (50,000 / 16,000)² ≈ 80 s for insertion sort, far over any time limit, so it is not an option.

**Slicing instead of a shared buffer.** I also considered `merge_sort(a[:mid])` and `merge_sort(a[mid:])` returning new lists. It is shorter to write, but it allocates new lists on every level, about n log n elements in total. One shared buffer allocates only n elements.

**Off-by-one in the middle.** With `mid = (lo + hi) // 2` the halves are `lo..mid` and `mid+1..hi`. If I used `mid` in both halves, a range of two elements would never shrink and the recursion would never stop.

## 3. Time Complexity

**O(n log n)**

Why: each call splits its range in half, so the recursion has about log₂ n levels (for n = 50,000 it is about 16). On every level, the merges together look at each element once, so one level costs O(n). In total O(n) × O(log n). As a formula: T(n) = 2·T(n/2) + O(n) = O(n log n). It does not depend on the order of the input: best, average and worst case are all O(n log n).

## Space Complexity

**O(n)**

Why: one buffer with n elements, plus the recursion stack with depth about log₂ n. O(n + log n) = O(n).

## 4. Reflection / Improvement

- O(n log n) is the best possible time for sorting by comparisons, but the memory can be reduced. **Heap sort** works inside the array: O(n log n) time and O(1) extra space, which matches "smallest space complexity possible" from the problem. The price: it is not stable and is usually slower in practice than merge sort.
- Values in this problem are limited to the range from -50,000 to 50,000, so **counting sort** is possible: count how many times each value appears and write the values out in order. Time O(n + k) and space O(k), where k = 100,001 is the size of the value range.
- **Quick sort** sorts in place and is fast on average, but its worst case is O(n²) time.

## Files

- `solution.py`: the solution (with a small self-test, run `python3 solution.py`)
- `trace.py`: prints the tracing (`python3 trace.py 5 2 3 1`)
- `brute_force_bench.py`: insertion sort vs merge sort timing
