import java.util.HashSet;
import java.util.Set;

public class LinkedListCycle {

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }

    // Version 1: remember visited nodes in a HashSet
    public static boolean hasCycleHashSet(ListNode head) {
        Set<ListNode> visited = new HashSet<>();
        ListNode cur = head;

        while (cur != null) {
            if (visited.contains(cur)) {
                return true;   // we are in this node the second time
            }
            visited.add(cur);
            cur = cur.next;
        }
        return false;          // we reached the end, no cycle
    }

    // Version 2: slow and fast pointers (Floyd's algorithm)
    public static boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }
        return false;
    }

    // helper: build a list from values; if pos >= 0, the last node points to the node with index pos
    static ListNode build(int[] vals, int pos) {
        if (vals.length == 0) {
            return null;
        }
        ListNode head = new ListNode(vals[0]);
        ListNode tail = head;
        ListNode cycleNode = (pos == 0) ? head : null;

        for (int i = 1; i < vals.length; i++) {
            tail.next = new ListNode(vals[i]);
            tail = tail.next;
            if (i == pos) {
                cycleNode = tail;
            }
        }
        tail.next = cycleNode;   // null when pos = -1, so there is no cycle
        return head;
    }

    public static void main(String[] args) {
        int[] a = {3, 2, 0, -4};

        System.out.println(hasCycleHashSet(build(a, 1)));            // true
        System.out.println(hasCycle(build(a, 1)));                   // true
        System.out.println(hasCycle(build(new int[]{1, 2}, 0)));     // true
        System.out.println(hasCycle(build(new int[]{1}, -1)));       // false
        System.out.println(hasCycle(build(new int[]{1, 2, 3}, -1))); // false
        System.out.println(hasCycle(null));                          // false
    }
}
