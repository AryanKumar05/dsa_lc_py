# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None or k == 0:
            return head
        
        # Convert linked list to list
        nodeList: List[ListNode] = []
        current = head
        while current is not None:
            nodeList.append(current)
            current = current.next
        
        # Determine the rotation
        n = len(nodeList)
        k = k % n
        if k == 0:
            return head  # Rotation results in same list

        # Rearrange nodes in list
        nodeList = nodeList[-k:] + nodeList[:-k]
        
        # Reconnect nodes to form a linked list
        for i in range(n - 1):
            nodeList[i].next = nodeList[i + 1]
        nodeList[-1].next = None
        
        return nodeList[0]
        