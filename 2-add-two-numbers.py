class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        val = []
        ll1 = l1
        ll2 = l2
        remainder = 0

        while ll1 or ll2:

            if ll1 and ll2:
                sum = ll1.val + ll2.val + remainder
            elif ll1 and not ll2:
                sum = ll1.val + remainder
            elif ll2 and not ll1:
                sum = ll2.val + remainder

            if sum >= 10:
                remainder = 1
                sum = sum % 10
            else:
                remainder = 0

            val.append(sum)
            ll1 = ll1.next if ll1 else None
            ll2 = ll2.next if ll2 else None

        if remainder:
            val.append(remainder)
        
        obj = ListNode(val[0])
        current_obj = obj

        for i in range(len(val)-1):

            while current_obj.next:
                current_obj = current_obj.next
            current_obj.next = ListNode(val[i+1])

        return obj


node_1 = ListNode(2, ListNode(4, ListNode(3)))
node_2 = ListNode(5, ListNode(6, ListNode(4)))
# node_2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
# node_1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
Solution().addTwoNumbers(node_1, node_2)