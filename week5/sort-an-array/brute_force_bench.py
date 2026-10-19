import random
import time

from solution import Solution


def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a


def timed(fn, arr):
    start = time.perf_counter()
    fn(arr)
    return time.perf_counter() - start


print(f"{'n':>7} | {'insertion sort':>15} | {'merge sort':>10}")
for n in (1000, 2000, 4000, 8000, 16000):
    arr = [random.randint(-50000, 50000) for _ in range(n)]
    t_ins = timed(insertion_sort, arr)
    t_mrg = timed(lambda a: Solution().sortArray(a[:]), arr)
    print(f"{n:>7} | {t_ins:>13.3f} s | {t_mrg:>8.4f} s")
