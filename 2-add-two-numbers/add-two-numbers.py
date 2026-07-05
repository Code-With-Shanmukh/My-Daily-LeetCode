# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node (starting point of answer)
        dummy = ListNode()

        # Current pointer
        current = dummy

        # Carry value
        carry = 0

        # Loop until both lists are finished
        while l1 or l2 or carry:

            # Take value from first list
            if l1:
                x = l1.val
            else:
                x = 0

            # Take value from second list
            if l2:
                y = l2.val
            else:
                y = 0

            # Add values
            total = x + y + carry

            # Calculate carry
            carry = total // 10

            # Create new node
            current.next = ListNode(total % 10)

            # Move current pointer
            current = current.next

            # Move first list
            if l1:
                l1 = l1.next

            # Move second list
            if l2:
                l2 = l2.next

        # Return answer
        return dummy.next