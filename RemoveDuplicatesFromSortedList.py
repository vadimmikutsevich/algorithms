class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(3)
five = ListNode(3)

one.next = two
two.next = three
three.next = four
four.next = five

head = one

def deleteDuplicates(head):
    i = head

    while i and i.next:
        if i.val == i.next.val:
            i = i.next.next
        else:
            i = i.next
            
    return head




print(deleteDuplicates(head))

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.