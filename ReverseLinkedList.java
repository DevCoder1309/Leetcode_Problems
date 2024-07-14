/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode temp = head;
        if (temp == null || temp.next == null) {
            return head;
        }
        ListNode temp2 = reverseList(temp.next);
        temp.next.next = head;
        head.next = null;
        return temp2;
    }
}