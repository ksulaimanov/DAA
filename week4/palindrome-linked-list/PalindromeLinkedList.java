import java.util.ArrayList;
import java.util.List;

public class PalindromeLinkedList {

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }

    // Version 1: brute force - copy values to an ArrayList and compare from both ends
    public static boolean isPalindromeBrute(ListNode head) {
        List<Integer> values = new ArrayList<>();
        for (ListNode cur = head; cur != null; cur = cur.next) {
            values.add(cur.val);
        }

        int left = 0;
        int right = values.size() - 1;
        while (left < right) {
            if (!values.get(left).equals(values.get(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    // Version 2: find the middle, reverse the second half, compare the halves, restore the list
    public static boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }

        // 1. find the end of the first half
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // 2. reverse the second half
        ListNode second = reverse(slow.next);

        // 3. compare the first half and the reversed second half
        ListNode p1 = head;
        ListNode p2 = second;
        boolean result = true;
        while (p2 != null) {
            if (p1.val != p2.val) {
                result = false;
                break;
            }
            p1 = p1.next;
            p2 = p2.next;
        }

        // 4. restore the original list
        slow.next = reverse(second);
        return result;
    }

    static ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    // Wrong attempt: compare Integer objects with != (works only for small numbers)
    public static boolean isPalindromeWrong(ListNode head) {
        List<Integer> values = new ArrayList<>();
        for (ListNode cur = head; cur != null; cur = cur.next) {
            values.add(cur.val);
        }

        int left = 0;
        int right = values.size() - 1;
        while (left < right) {
            if (values.get(left) != values.get(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
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
        System.out.println(isPalindromeBrute(build(1, 2, 2, 1)));   // true
        System.out.println(isPalindromeBrute(build(1, 2)));         // false
        System.out.println(isPalindrome(build(1, 2, 2, 1)));        // true
        System.out.println(isPalindrome(build(1, 2, 3, 2, 1)));     // true
        System.out.println(isPalindrome(build(1, 2)));              // false
        System.out.println(isPalindrome(build(1)));                 // true

        ListNode list = build(1, 2, 3, 2, 1);
        isPalindrome(list);
        System.out.println(show(list));                             // [1, 2, 3, 2, 1] (list is restored)

        System.out.println(isPalindromeWrong(build(1000, 1000)));   // false (wrong attempt, should be true)
        System.out.println(isPalindromeBrute(build(1000, 1000)));   // true
    }
}
