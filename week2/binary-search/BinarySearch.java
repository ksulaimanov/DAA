public class BinarySearch {

    // Version 1: linear search (my first solution), O(n)
    public static int searchLinear(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }

    // Version 2: binary search, O(log n)
    public static int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {-1, 0, 3, 5, 9, 12};

        System.out.println(searchLinear(nums, 9));  // 4
        System.out.println(searchLinear(nums, 2));  // -1
        System.out.println(search(nums, 9));        // 4
        System.out.println(search(nums, 2));        // -1
    }
}
