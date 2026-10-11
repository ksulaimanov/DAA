public class IntersectionOfTwoLinkedLists {

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }

    // Version 1: brute force - compare every node of A with every node of B (by reference)
    public static ListNode getIntersectionNodeBrute(ListNode headA, ListNode headB) {
        for (ListNode a = headA; a != null; a = a.next) {
            for (ListNode b = headB; b != null; b = b.next) {
                if (a == b) {
                    return a;
                }
            }
        }
        return null;
    }

    // Version 2: two pointers, when a pointer reaches the end it goes to the head of the other list
    public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA;
        ListNode b = headB;

        while (a != b) {
            a = (a == null) ? headB : a.next;
            b = (b == null) ? headA : b.next;
        }
        return a;   // the intersection node, or null if there is no intersection
    }

    // Wrong attempt: compare values instead of nodes
    public static ListNode getIntersectionNodeWrong(ListNode headA, ListNode headB) {
        for (ListNode a = headA; a != null; a = a.next) {
            for (ListNode b = headB; b != null; b = b.next) {
                if (a.val == b.val) {
                    return a;
                }
            }
        }
        return null;
    }

    // helper: build a list from values and attach a tail (the tail can be shared with another list)
    static ListNode buildWithTail(ListNode tail, int... vals) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : vals) {
            cur.next = new ListNode(v);
            cur = cur.next;
        }
        cur.next = tail;
        return dummy.next;
    }

    static ListNode build(int... vals) {
        return buildWithTail(null, vals);
    }

    static String val(ListNode node) {
        return node == null ? "null" : String.valueOf(node.val);
    }

    public static void main(String[] args) {
        // A = 4 -> 1 -> [8 -> 4 -> 5], B = 5 -> 6 -> 1 -> [8 -> 4 -> 5], the part in [] is shared
        ListNode common = build(8, 4, 5);
        ListNode listA = buildWithTail(common, 4, 1);
        ListNode listB = buildWithTail(common, 5, 6, 1);

        System.out.println(val(getIntersectionNodeBrute(listA, listB)));  // 8
        System.out.println(val(getIntersectionNode(listA, listB)));       // 8
        System.out.println(val(getIntersectionNodeWrong(listA, listB)));  // 4  (wrong attempt)

        ListNode listC = build(2, 6, 4);
        ListNode listD = build(1, 5);
        System.out.println(val(getIntersectionNodeBrute(listC, listD)));  // null
        System.out.println(val(getIntersectionNode(listC, listD)));       // null
    }
}
