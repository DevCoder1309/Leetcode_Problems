class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int ans = nums[0];
        while (l <= r) {
            int mid = (l + r) / 2;
            if (mid > 0 && nums[mid] <= nums[mid - 1]) {
                ans = nums[mid];
                break;
            }
            if (mid < nums.length - 1 && nums[mid] > nums[mid + 1]) {
                ans = nums[mid + 1];
                break;
            }
            if (nums[mid] >= nums[l]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ans;
    }
}