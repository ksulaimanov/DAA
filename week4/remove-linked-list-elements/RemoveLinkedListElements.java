import java.util.ArrayList;
import java.util.List;

public class RemoveLinkedListElements {

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }

    // Version 1: brute force - collect the values we keep, then build a new list
    public static ListNode removeElementsBrute(ListNode head, int val) {
        List<Integer> values = new ArrayList<>();
        for (ListNode cur = head; cur != null; cur = cur.next) {
            if (cur.val != val) {
                values.add(cur.val);
            }
        }

        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        for (int v : values) {
            tail.next = new ListNode(v);
            tail = tail.next;
        }
        return dummy.next;
    }

    // Version 2: in place, with a dummy node before the head
    public static ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy;

        while (cur.next != null) {
            if (cur.next.val == val) {
                cur.next = cur.next.next;   // delete the next node, stay on cur
            } else {
                cur = cur.next;             // keep the next node, go forward
            }
        }
        return dummy.next;
    }

    // Wrong attempt: no dummy node, so the head is never checked
    public static ListNode removeElementsWrong(ListNode head, int val) {
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            if (cur.next.val == val) {
                cur.next = cur.next.next;
            } else {
                cur = cur.next;
            }
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
        System.out.println(show(removeElementsBrute(build(1, 2, 6, 3, 4, 5, 6), 6)));  // [1, 2, 3, 4, 5]
        System.out.println(show(removeElements(build(1, 2, 6, 3, 4, 5, 6), 6)));       // [1, 2, 3, 4, 5]
        System.out.println(show(removeElements(build(7, 7, 7, 7), 7)));                // []
        System.out.println(show(removeElements(build(), 1)));                          // []
        System.out.println(show(removeElementsWrong(build(6, 1, 6, 2), 6)));           // [6, 1, 2]  (wrong attempt)
        System.out.println(show(removeElements(build(6, 1, 6, 2), 6)));                // [1, 2]
    }
}
