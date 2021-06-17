from singly_linked import ListNode

def makeLinkedList(lst):
    curr = None
    next = None

    for i in lst[::-1]:
        curr = ListNode(i)
        curr.next = next
        next = curr

    return curr

a = makeLinkedList([1, 2, 3, 4])

def swapPairs(head):
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:

        # I am going to explain with the example in the first loop.
        # Swapping the order of the pair: 1(--head), 2(--b), 3 -> 2, 1, 3

        b = head.next # b is now 2
        head.next = b.next # head(--1) linked with 3
        b.next = head # b linked with 1

        prev.next = b # prev linked with the first node (--2) of linked list

        head = head.next # head becomes 3
        prev = prev.next.next

    return root.next

print(swapPairs(a))
