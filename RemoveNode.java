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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // replace my n value
        ListNode temp = head;
        ListNode temp2 = head;
        ListNode temp3 = head;
        int count = 0;
        if (head.next == null) {
            return null;
        }
        while (temp != null) {
            count++;
            temp = temp.next;
        }
        n = count - n + 1;
        if (n == 1) {
            head = head.next;
            return head;
        }
        int count2 = 1;
        int count3 = 1;
        while (count3 != n - 1 && temp3 != null) {
            temp3 = temp3.next;
            count3++;
        }
        while (count2 != n) {
            head = head.next;
            count2++;
        }
        if (head != null && temp3 != null) {
            temp3.next = head.next;
        }
        return temp2;
    }
}