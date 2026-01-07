"""
LeetCode 21 - Merge Two Sorted Lists

Problem:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list and return its head.

The new list should be made by splicing together the nodes of the first two lists.

Time Complexity: O(n + m) ; where n and m is the size of list1 and list2, respectively
Space Complexity: O(1)  (iterative, in-place)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node simplifies edge cases (empty list, first insertion)
        dummy = ListNode(0)
        curr = dummy  # Pointer used to build the merged list

        # Traverse both lists while neither is exhausted
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1       # Attach smaller node
                list1 = list1.next      # Advance list1
            else:
                curr.next = list2
                list2 = list2.next      # Advance list2

            curr = curr.next            # Advance merged list pointer

        # At least one list is now None
        # Attach the remaining nodes directly
        curr.next = list1 if list1 else list2

        return dummy.next
