from solution import build


def sort_list_no_cut(head):
    if head is None or head.next is None:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    # BUG: forgot "slow.next = None", so the first half still contains the second half
    left = sort_list_no_cut(head)
    right = sort_list_no_cut(second)
    return left


try:
    sort_list_no_cut(build([2, 1]))
except RecursionError as e:
    print("RecursionError:", e)
