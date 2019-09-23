# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = []
        while head:
            l[len(l):], head = [head], head.next
        if l:
            l[-1].next, l[-1 - k % len(l)].next = l[0], None

        return l[- k % len(l)] if l else None
