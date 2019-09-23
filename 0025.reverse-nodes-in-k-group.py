# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = left = right = head

        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1

            if count == k:
                pre, cur = right, left
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, left = pre, left, right
            else:
                return dummy.next
