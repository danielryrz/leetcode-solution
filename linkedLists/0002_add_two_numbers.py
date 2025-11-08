"""
Problem: Add Two Numbers (LeetCode #2)
---------------------------------------
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zeros,
except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
"""

# Definition for singly-linked list.
# LeetCode automatically provides this, but included here for clarity:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists and returns the result
        as a new linked list.

        Args:
            l1 (ListNode): Head of the first linked list.
            l2 (ListNode): Head of the second linked list.

        Returns:
            ListNode: Head of the new linked list representing the sum.
        """

        carry = 0                   # Stores carry-over value during addition
        dummy = ListNode(0)         # Dummy head node to simplify list construction
        current = dummy             # Pointer used to build the result list

        # Loop continues until both lists are fully processed and no carry remains
        while l1 or l2 or carry:
            # Get the current digit values from both lists (use 0 if one list is shorter)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute sum of digits + carry
            total = val1 + val2 + carry

            # Update carry for the next iteration
            carry = total // 10

            # Extract the actual digit to store in the current node
            digit = total % 10

            # Create a new node with the computed digit
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes in l1 and l2 (if available)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # The first node (dummy) is a placeholder, so return the next node
        return dummy.next


"""
Time Complexity:  O(max(m, n))
------------------------------
We traverse each list once, where m and n are the lengths of l1 and l2.
Each operation (addition, carry computation, node creation) takes constant time.

Space Complexity: O(max(m, n))
------------------------------
We create a new linked list to store the result, with at most one extra node
if there’s a carry at the end.
"""
