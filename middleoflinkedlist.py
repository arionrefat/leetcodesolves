# time complexity O(n) and space complexity is 0(1)


def middleOfList(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
