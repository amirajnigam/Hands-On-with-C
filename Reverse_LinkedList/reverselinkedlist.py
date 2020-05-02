class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
            head = prev
            
        return head