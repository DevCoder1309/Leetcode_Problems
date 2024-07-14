import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int p = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[p] == nums[i]) {
                return true;
            }
            p++;
        }
        return false;
    }
}