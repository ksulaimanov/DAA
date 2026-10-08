import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MergeTwoSortedLists {

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }

    // Version 1: brute force - collect all values, sort them, build a new list
    public static ListNode mergeBruteForce(ListNode list1, ListNode list2) {
        List<Integer> values = new ArrayList<>();

        for (ListNode cur = list1; cur != null; cur = cur.next) {
            values.add(cur.val);
        }
        for (ListNode cur = list2; cur != null; cur = cur.next) {
            values.add(cur.val);
        }

        Collections.sort(values);

        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        for (int v : values) {
            tail.next = new ListNode(v);
            tail = tail.next;
        }
        return dummy.next;
    }

    // Version 2: two pointers, reuse the existing nodes
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        // one list is finished, attach the rest of the other one
        tail.next = (list1 != null) ? list1 : list2;
        return dummy.next;
    }

    // helper: build a list from values
    static ListNode build(int... vals) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        for (int v : vals) {
            tail.next = new ListNode(v);
            tail = tail.next;
        }
        return dummy.next;
    }

    // helper: list to string
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
        // fresh lists for every test, because mergeTwoLists changes the links
        System.out.println(show(mergeBruteForce(build(1, 2, 4), build(1, 3, 4)))); // [1, 1, 2, 3, 4, 4]
        System.out.println(show(mergeTwoLists(build(1, 2, 4), build(1, 3, 4))));   // [1, 1, 2, 3, 4, 4]
        System.out.println(show(mergeTwoLists(build(), build())));                 // []
        System.out.println(show(mergeTwoLists(build(), build(0))));                // [0]
    }
}
