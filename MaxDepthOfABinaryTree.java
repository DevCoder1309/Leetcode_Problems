/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        TreeNode temp = root;
        if (root == null) {
            return 0;
        }
        int left = maxDepth(temp.left);
        int right = maxDepth(temp.right);
        if (left >= right) {
            return left + 1;
        }
        return right + 1;
    }
}