# if the linked list has cycle or not
# time complexity is 0(n) and space complexity is O(1)


def hasCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
