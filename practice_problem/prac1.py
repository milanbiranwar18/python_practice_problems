# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.
# Example
# 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example
# 3:
#
# Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
# Output: [8, 9, 9, 9, 0, 0, 0, 1]


class Node():
    def __init__(self, val):
        self.val = val
        self.ref = None


# class LL():
# def __init__(self):
#     self.head = None
#
# def add_data(self, data):
#     new_node = Node(data)
#     new_node.ref = self.head
#     self.head = new_node

class LL():
    def add_two_num(self, l1: Node, l2: Node) -> Node:
        carry = 0
        result = Node(0)
        pointer = result

        while l1 or l2 or carry:

            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0

            sum = first_num + second_num + carry
            num = sum % 10
            carry = sum // 10
            pointer.ref = Node(num)
            pointer = pointer.ref

            l1 = l1.ref if l1 else None
            l2 = l2.ref if l2 else None

        return result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        carry, val = divmod(val, 10)
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     dummy = ListNode(0)
#     curr = dummy
#     carry = 0
#
#     while l1 or l2:
#         x = l1.val if l1 else 0
#         y = l2.val if l2 else 0
#         summ = carry + x + y
#         carry = summ // 10
#         curr.next = ListNode(summ % 10)
#         curr = curr.next
#         if l1: l1 = l1.next
#         if l2: l2 = l2.next
#
#     if carry > 0:
#         curr.next = ListNode(carry)
#
#     return dummy.next


if __name__ == '__main__':
    # ll = LL()
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    # ll.add_two_num(l1, l2)

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=' ')
        result = result.next