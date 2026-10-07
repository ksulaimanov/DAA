# First Bad Version

## Problem
We have versions of a product numbered from 1 to n. At some version the product became bad, and all versions after it are bad too (good, good, ..., bad, bad). We have a function `isBadVersion(version)` that tells if a version is bad. We need to find the first bad version.

## Approach
I wrote two versions.

**Version 1: linear search (my first solution).**
I check versions one by one from 1 to n. The first version where `isBadVersion` returns `true` is the answer.

**Version 2: binary search.**
The versions look like `false false false true true true`, so I can search for the border between `false` and `true`:
1. Set `left = 1` and `right = n`.
2. Calculate `mid = left + (right - left) / 2`.
3. If `isBadVersion(mid)` is `true`, then `mid` can be the first bad version, but there can be bad versions on the left too. So `right = mid`.
4. If it is `false`, the first bad version is on the right, so `left = mid + 1`.
5. Repeat while `left < right`. At the end `left == right` and this is the answer.

The difference from the classic binary search: here I do not return when I find a bad version, because I need the first one, not any of them. I use `left + (right - left) / 2` to avoid integer overflow, because n can be up to 2^31 - 1.

## Time Complexity
- Linear search: **O(n)**. In the worst case the last version is the first bad one, so I call `isBadVersion` n times.
- Binary search: **O(log n)**. Each step cuts the range of possible answers in half (n, n/2, n/4, ..., 1), so there are about log2(n) calls of `isBadVersion`.

## Space Complexity
**O(1)** for both versions. I use only several integer variables (`i`, `left`, `right`, `mid`), and I do not create extra arrays or use recursion.

## Reflection / Improvement
The linear solution does not use the fact that after the first bad version all versions are bad. Because of this order I can use binary search and reduce the number of API calls from O(n) to O(log n). The space complexity stays O(1).
