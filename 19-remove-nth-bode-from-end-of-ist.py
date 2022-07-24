from multiprocessing.connection import Listener
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Method 1
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# head = ListNode(1, ListNode(2, ListNode(3)))
# head = ListNode(1)
n = 2
Solution().removeNthFromEnd(head, n)