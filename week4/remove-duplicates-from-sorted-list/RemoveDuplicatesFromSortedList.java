public class RemoveDuplicatesFromSortedList {

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }

    // Version 1: brute force - for every node remove all later nodes with the same value
    public static ListNode deleteDuplicatesBrute(ListNode head) {
        ListNode cur = head;
        while (cur != null) {
            ListNode runner = cur;
            while (runner.next != null) {
                if (runner.next.val == cur.val) {
                    runner.next = runner.next.next;   // delete the duplicate
                } else {
                    runner = runner.next;
                }
            }
            cur = cur.next;
        }
        return head;
    }

    // Version 2: one pass, we use the fact that the list is sorted
    public static ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            if (cur.val == cur.next.val) {
                cur.next = cur.next.next;   // delete the duplicate, stay on the same node
            } else {
                cur = cur.next;             // different value, go forward
            }
        }
        return head;
    }

    // Wrong attempt: move cur forward even after deleting a node
    public static ListNode deleteDuplicatesWrong(ListNode head) {
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            if (cur.val == cur.next.val) {
                cur.next = cur.next.next;
            }
            cur = cur.next;
        }
        return head;
    }

    static ListNode build(int... vals) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        for (int v : vals) {
            tail.next = new ListNode(v);
            tail = tail.next;
        }
        return dummy.next;
    }

    static String show(ListNode head) {
        StringBuilder sb = new StringBuilder("[");
        while (head != null) {
            sb.append(head.val);
            if (head.next != null) {
                sb.append(", ");
            }
            head = head.next;
        }
        return sb.append("]").toString();
    }

    public static void main(String[] args) {
        System.out.println(show(deleteDuplicatesBrute(build(1, 1, 2, 3, 3))));  // [1, 2, 3]
        System.out.println(show(deleteDuplicates(build(1, 1, 2, 3, 3))));       // [1, 2, 3]
        System.out.println(show(deleteDuplicates(build(1, 1, 1, 2))));          // [1, 2]
        System.out.println(show(deleteDuplicates(build())));                    // []
        System.out.println(show(deleteDuplicatesWrong(build(1, 1, 1, 2))));     // [1, 1, 2]  (wrong attempt)
    }
}
