from singly_linked import ListNode

def isPalindrome(head):
    q = list()
    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1: # comare the first element of the list to the last element of the list repeatedly
        if q.pop(0) != q.pop(): # q.pop(0) pop the first element of q, q.pop() pop the last element of q
            return False

    return True

# Input: [1, 3, 3, 1]

test = ListNode(1)
second = ListNode(3)
third = ListNode(3)
fourth = ListNode(1)

test.next = second
second.next = third
third.next = fourth

print(isPalindrome(test))
# Answer: True
