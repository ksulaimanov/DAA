# Binary Search

## Problem
We have a sorted array of integers `nums` and a number `target`. We need to return the index of `target` in the array. If `target` is not in the array, we return `-1`.

## Approach
I wrote two versions.

**Version 1: linear search (my first solution).**
I go through the array from left to right and compare each element with `target`. If they are equal, I return the index. If the loop ends and nothing was found, I return `-1`.

**Version 2: binary search.**
The array is sorted, so I can look at the middle element and throw away half of the array every time:
1. Set `left = 0` and `right = nums.length - 1`.
2. Calculate `mid = left + (right - left) / 2`.
3. If `nums[mid] == target`, return `mid`.
4. If `nums[mid] < target`, the target can only be on the right side, so `left = mid + 1`.
5. If `nums[mid] > target`, the target can only be on the left side, so `right = mid - 1`.
6. Repeat while `left <= right`. If the loop ends, return `-1`.

I use `left + (right - left) / 2` instead of `(left + right) / 2` to avoid integer overflow.

## Time Complexity
- Linear search: **O(n)**. In the worst case (the target is the last element or is not in the array) the algorithm checks every element once. If there are n elements, there are n checks.
- Binary search: **O(log n)**. After each step the search area becomes two times smaller: n, n/2, n/4, ..., 1. This takes about log2(n) steps.

## Space Complexity
**O(1)** for both versions. I use only a few variables (`i`, `left`, `right`, `mid`). Their number does not depend on the size of the array. I do not create new arrays and I do not use recursion.

## Reflection / Improvement
Linear search does not use the fact that the array is sorted, so it is O(n). Binary search uses it and improves the time to O(log n). For example, for n = 1,000,000 linear search may need up to 1,000,000 checks, but binary search needs only about 20. Space stays O(1). Binary search works only on sorted data.
