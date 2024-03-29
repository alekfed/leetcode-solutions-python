# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappop, heapreplace, heapify


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        zero = node = ListNode(0)
        heap = [(n.val, n) for n in lists if n]
        heapify(heap)

        while heap:
            v, n = heap[0]
            if n.next is None:
                heappop(heap)
            else:
                heapreplace(heap, (n.next.val, n.next))
            node.next = n
            node = node.next

        return zero.next
