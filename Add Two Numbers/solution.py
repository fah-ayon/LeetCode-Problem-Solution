class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:

            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1 + n2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next


# Tester
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked(lst):
    dummy = ListNode(0)
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1_ll = list_to_linked(l1)
l2_ll = list_to_linked(l2)

res = Solution().addTwoNumbers(l1_ll, l2_ll)
print(linked_to_list(res))  