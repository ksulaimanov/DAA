import sys


def trace(a, depth=0):
    pad = "  " * depth
    if len(a) <= 1:
        print(f"{pad}base  {a}")
        return a
    mid = (len(a) + 1) // 2  # left half gets the extra element
    print(f"{pad}split {a} -> {a[:mid]} | {a[mid:]}")
    left = trace(a[:mid], depth + 1)
    right = trace(a[mid:], depth + 1)
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:] + right[j:]
    print(f"{pad}merge {left} + {right} -> {merged}")
    return merged


if __name__ == "__main__":
    data = [int(x) for x in sys.argv[1:]] or [5, 2, 3, 1]
    print("input:", data)
    print("result:", trace(data))
