from singly_linked import ListNode

t1 = ListNode(2)
t1_second = ListNode(4)
t1_third = ListNode(3)
t1.next = t1_second
t1_second.next = t1_third

t2 = ListNode(5)
t2_second = ListNode(6)
t2_third = ListNode(4)
t2.next = t2_second
t2_second.next = t2_third

def reverse_list(l_list):
    curr = l_list
    prev = None

    while curr:
        next, curr.next = curr.next, prev
        prev, curr = curr, next
    return prev

def list_to_int(q_list):
    q = str()
    s = q_list

    while s is not None:
        q += str(s.val)
        s = s.next

    q = int(q)

    return q


def add_two_numbers(l1, l2):

    a = reverse_list(l1)
    b = reverse_list(l2)

    c = list_to_int(a)
    d = list_to_int(b)

    e = c + d
    e = str(e)

    q = [i for i in e]

    curr = None
    next = None

    for i in q[::-1]:
        curr = ListNode(i)
        curr.next = next
        next = curr

    return curr

print(add_two_numbers(t1, t2))
