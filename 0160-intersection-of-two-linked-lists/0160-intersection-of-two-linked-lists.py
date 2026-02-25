# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        b_elements=set()

        a=headA
        b=headB
        while b is not None:
            b_elements.add(b)
            b=b.next
        while a is not None:
            if a not in b_elements:
                a=a.next
            else:
                return a
        return None

        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        