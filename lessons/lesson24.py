# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # validation
        if head is None or head.next is None:
            return head

        # init
        first = head
        second = head.next

        # swap
        first.next = self.swapPairs(second.next)
        second.next = first

        return second
