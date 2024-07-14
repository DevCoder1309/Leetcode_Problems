class Solution {
    public int search(int[] nums, int target) {
        // Binary search
        int l = -1;
        int last = nums.length - 1;
        int first = 0;
        int mid;
        while (first <= last) {
            mid = (first + last) / 2;
            if (target == nums[mid]) {
                l = mid;
                break;
            }
            if (target < nums[mid]) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }
        return l;
    }
}
