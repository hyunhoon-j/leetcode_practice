from singly_linked import ListNode

l_lst = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

l_lst.next = second
second.next = third
third.next = fourth
fourth.next = fifth

def reverseList(head):
    curr = head
    prev = None

    while curr:
        next, curr.next = curr.next, prev # curr.next in the right-hand side refers to specific node
        curr, prev = next, curr

    return prev

print(reverseList(l_lst))
