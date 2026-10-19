import sys

from solution import Solution, build, to_list


def fmt(head):
    values = to_list(head)
    return "[" + " -> ".join(str(v) for v in values) + "]"


def trace(head, depth=0):
    pad = "  " * depth
    if head is None or head.next is None:
        print(f"{pad}base  {fmt(head)}")
        return head
    whole = fmt(head)
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    middle = slow.val
    second = slow.next
    slow.next = None  # cut the list after the middle node
    print(f"{pad}split {whole}  (slow stops at {middle}) -> {fmt(head)} | {fmt(second)}")
    left = trace(head, depth + 1)
    right = trace(second, depth + 1)
    before = f"{fmt(left)} + {fmt(right)}"
    merged = Solution()._merge(left, right)
    print(f"{pad}merge {before} -> {fmt(merged)}")
    return merged


if __name__ == "__main__":
    data = [int(x) for x in sys.argv[1:]] or [4, 2, 1, 3]
    print("input:", fmt(build(data)))
    print("result:", fmt(trace(build(data))))
