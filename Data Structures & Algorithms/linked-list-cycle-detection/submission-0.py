# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        # record nodes in dict
        # if node.next is in dict, return true, else add

        curr = head
        while curr:
            if curr.next in d:
                return True
            else:
                d[curr] = 1
            curr = curr.next
        return False