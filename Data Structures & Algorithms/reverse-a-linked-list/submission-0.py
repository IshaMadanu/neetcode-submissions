# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            # reverse the links
                # set curr's next val to the one prev
                # update prev to be current node and curr to be next node
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head
