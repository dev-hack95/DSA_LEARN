class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    ptr = ListNode(0) 
    curr = ptr

    carry = 0 

    while l1 or l2:
        sum = carry

        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        digit = sum % 10

        curr.next = ListNode(digit)
        curr = curr.next

    if carry > 0:
        curr.next = ListNode(carry)

    return ptr.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next

l1 = ListNode(0)
l2 = ListNode(0)

result = add_num(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
  
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
