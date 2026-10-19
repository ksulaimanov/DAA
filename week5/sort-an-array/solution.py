from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        buf = [0] * len(nums)  # one buffer, reused by every merge
        self._sort(nums, buf, 0, len(nums) - 1)
        return nums

    def _sort(self, a, buf, lo, hi):
        if lo >= hi:  # 0 or 1 element: already sorted
            return
        mid = (lo + hi) // 2
        self._sort(a, buf, lo, mid)
        self._sort(a, buf, mid + 1, hi)
        self._merge(a, buf, lo, mid, hi)

    def _merge(self, a, buf, lo, mid, hi):
        i, j, k = lo, mid + 1, lo
        while i <= mid and j <= hi:
            if a[i] <= a[j]:
                buf[k] = a[i]
                i += 1
            else:
                buf[k] = a[j]
                j += 1
            k += 1
        while i <= mid:
            buf[k] = a[i]
            i += 1
            k += 1
        while j <= hi:
            buf[k] = a[j]
            j += 1
            k += 1
        a[lo:hi + 1] = buf[lo:hi + 1]


if __name__ == "__main__":
    import random

    tests = [[], [1], [2, 1], [5, 2, 3, 1], [5, 1, 1, 2, 0, 0], [3, 3, 3], list(range(10, 0, -1))]
    for t in tests:
        assert Solution().sortArray(t[:]) == sorted(t), t
    for _ in range(500):
        t = [random.randint(-50, 50) for _ in range(random.randint(0, 40))]
        assert Solution().sortArray(t[:]) == sorted(t), t
    print("sort-an-array: all tests passed")
