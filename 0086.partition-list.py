# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = node1 = ListNode(0)
        head2 = node2 = ListNode(0)

        while head:
            if head.val < x:
                node1.next = head
                node1 = node1.next
            else:
                node2.next = head
                node2 = node2.next
            head = head.next

        node2.next = None
        node1.next = head2.next

        return head1.next
