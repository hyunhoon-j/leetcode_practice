from singly_linked import ListNode

# set up l1_list

l1_list = ListNode(1)
l1_second = ListNode(2)
l1_third = ListNode(4)

l1_list.next = l1_second
l1_second.next = l1_third

# set up l2_list
l2_list = ListNode(1)
l2_second = ListNode(3)
l2_third = ListNode(4)

l2_list.next = l2_second
l2_second.next = l2_third


def mergeTwoLists(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2) # Recursive case in if statement
    return l1

result = mergeTwoLists(l1_list, l2_list)

q = list()

while result is not None:
    q.append(result.val)
    result = result.next

print(q)
# Answer: [1, 1, 2, 3, 4, 4]
