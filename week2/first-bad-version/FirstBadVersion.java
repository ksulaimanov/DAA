public class FirstBadVersion {

    // Imitation of the LeetCode API: versions starting from badVersion are bad
    private static int badVersion;

    private static boolean isBadVersion(int version) {
        return version >= badVersion;
    }

    // Version 1: linear search (my first solution), O(n) calls of isBadVersion
    public static int firstBadVersionLinear(int n) {
        for (int i = 1; i <= n; i++) {
            if (isBadVersion(i)) {
                return i;
            }
        }
        return -1; // never happens, the problem guarantees a bad version exists
    }

    // Version 2: binary search, O(log n) calls of isBadVersion
    public static int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (isBadVersion(mid)) {
                right = mid;       // mid can be the answer, look on the left including mid
            } else {
                left = mid + 1;    // mid is good, the answer is on the right
            }
        }
        return left;
    }

    public static void main(String[] args) {
        badVersion = 4;
        System.out.println(firstBadVersionLinear(5)); // 4
        System.out.println(firstBadVersion(5));       // 4

        badVersion = 1;
        System.out.println(firstBadVersion(1));       // 1
        System.out.println(firstBadVersion(10));      // 1

        badVersion = 10;
        System.out.println(firstBadVersion(10));      // 10
    }
}
