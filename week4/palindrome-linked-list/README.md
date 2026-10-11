# Palindrome Linked List

## Problem
We have a singly linked list. We need to check if it is a palindrome, which means it reads the same from the beginning to the end and from the end to the beginning (for example `1 -> 2 -> 2 -> 1`).

## Approach
I wrote two versions.

**Version 1: brute force (my first solution).**
A linked list can only be read in one direction, so I copy all values into an `ArrayList`. Then I use two indexes, `left` at the start and `right` at the end, compare the values and move the indexes to the center. If some pair is different, the answer is `false`. If I reach the center, the answer is `true`. For comparing the values I use `equals`.

**Version 2: reverse the second half.**
1. Find the end of the first half with `slow` and `fast` pointers (`slow` moves 1 step, `fast` moves 2 steps). When `fast` reaches the end, `slow` is in the middle.
2. Reverse the second half of the list (starting from `slow.next`).
3. Compare the first half with the reversed second half node by node. If the list has an odd length, the middle node is not compared.
4. Reverse the second half again to restore the list, then return the result.

### Tracing (version 2)
Example: `1 -> 2 -> 3 -> 2 -> 1`

Step 1, find the middle:

| Iteration | slow | fast |
|-----------|------|------|
| start | 1 (index 0) | 1 (index 0) |
| 1 | 2 (index 1) | 3 (index 2) |
| 2 | 3 (index 2) | 1 (index 4) |

`fast.next` is `null`, so the loop stops. `slow` is at 3 (the middle).

Step 2, reverse the second half: `2 -> 1` becomes `1 -> 2`.

Step 3, compare: `p1` goes `1, 2`, `p2` goes `1, 2`. All pairs are equal (1 = 1, 2 = 2), `p2` becomes `null`, so the result is `true`. The middle 3 is not compared.

Step 4, restore: reverse the second half again, the list is `1 -> 2 -> 3 -> 2 -> 1` again.

Another example, `1 -> 2 -> 2 -> 3`: `slow` stops at the first 2, the second half `2 -> 3` is reversed to `3 -> 2`, and the first comparison 1 and 3 is different, so the result is `false`.

### Tracing (version 1)
Example: `1 -> 2 -> 2 -> 1`. Values `[1, 2, 2, 1]`. `left = 0, right = 3`: 1 and 1 are equal. `left = 1, right = 2`: 2 and 2 are equal. Now `left = 2, right = 1`, the loop ends, result `true`.

## Challenges
- In version 1 I first compared the values with `!=` (method `isPalindromeWrong`). For `1000 -> 1000` it returned `false`. The values in the `ArrayList<Integer>` are objects, and `!=` compares objects, not numbers. It works only for small numbers (Java caches the numbers from -128 to 127). I changed it to `equals`.
- I thought about reversing the whole list and comparing it with the original. It does not work, because reversing in place changes the original links, so there is nothing to compare with. To keep the original I would need to copy the list, which uses O(n) memory, and then it is no better than version 1. So I reverse only the second half.
- Reversing the second half changes the input list, so I reverse it back at the end.

## Time Complexity
**O(n)** for both versions, where n is the number of nodes.
- Version 1: one pass to copy the values (n) and up to n / 2 comparisons.
- Version 2: finding the middle takes about n / 2 steps, reversing the second half n / 2, comparing n / 2, restoring n / 2. It is about 2n steps in total, and constants are ignored in Big O, so it is O(n).

## Space Complexity
- Version 1: **O(n)**, because the `ArrayList` stores all n values.
- Version 2: **O(1)**. I only use a few pointers (`slow`, `fast`, `prev`, `cur`, `p1`, `p2`) and I reverse the nodes in place.

## Reflection / Improvement
Both versions have the same time O(n), but version 2 removes the extra memory: O(n) becomes O(1). The price is a more complex code and a temporary change of the list (which I restore). A recursive solution is also possible, but it uses the call stack and needs O(n) memory, so it is not better than version 1 in space.
