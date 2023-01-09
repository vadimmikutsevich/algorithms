class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five

head = one


def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
    
print(middleNode(head))


# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.