import java.util.*;
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merge = new int[nums1.length + nums2.length];
        int i = 0, j = 0, k = 0;
        while (i < nums1.length) {
            merge[k++] = nums1[i++];
        }
        while (j < nums2.length) {
            if (merge[j] <= nums2[j]) {
                merge[k++] = nums2[j++];
            }

        }
        Arrays.sort(merge);
        if (merge.length % 2 != 0) {
            return merge[(merge.length) / 2];
        } else {
            int mid = merge.length / 2;
            return (merge[mid] + merge[mid - 1]) / 2.0;
        }
    }
}