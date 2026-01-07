# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem:
        Reverse a singly linked list.

        Approach:
        Iterative pointer reversal.

        We traverse the list once and reverse the direction of each node's `next`
        pointer so it points to the previous node instead of the next one.

        Steps:
        - Initialize `prev` as None (this will become the new tail).
        - Use `curr` to traverse the list.
        - Temporarily store the next node.
        - Reverse the `next` pointer.
        - Move `prev` and `curr` one step forward.

        Time Complexity:
        O(n) — each node is visited once.

        Space Complexity:
        O(1) — in-place reversal, no extra data structures used.
        """

        prev = None #set prev to None (this will be the new tail to which the curr will connect, in the first iteration)
        curr = head

        while curr:
            next_node = curr.next   # store next node
            curr.next = prev        # reverse pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev
