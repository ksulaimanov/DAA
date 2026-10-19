from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # 0 or 1 node: already sorted
            return head
        second = self._split(head)  # cuts the list, returns head of 2nd half
        left = self.sortList(head)
        right = self.sortList(second)
        return self._merge(left, right)

    def _split(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None  # cut: the first half must end here
        return second

    def _merge(self, a, b):
        dummy = tail = ListNode()
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next


def build(values):
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    import random

    tests = [[], [1], [2, 1], [4, 2, 1, 3], [-1, 5, 3, 4, 0], [3, 3, 3], list(range(10, 0, -1))]
    for t in tests:
        assert to_list(Solution().sortList(build(t))) == sorted(t), t
    for _ in range(500):
        t = [random.randint(-50, 50) for _ in range(random.randint(0, 40))]
        assert to_list(Solution().sortList(build(t))) == sorted(t), t
    print("sort-list: all tests passed")
