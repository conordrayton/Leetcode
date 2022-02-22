# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ListNode3 = ListNode(3, None)
ListNode2 = ListNode(4, ListNode3)
ListNode1 = ListNode(2, ListNode2)
l_one = [ListNode1, ListNode2, ListNode3]

ListNodez = ListNode(4, None)
ListNodey = ListNode(6, ListNodez)
ListNodex = ListNode(5, ListNodey)
l_two = [ListNodex, ListNodey, ListNodez]


def addTwoNumbers(l1: [ListNode], l2: [ListNode]) -> [ListNode]:
    i = 0
    output = []
    carry = 0
    value = 0
    while i < l1.__len__() and i < l2.__len__():
        value += l1[i].val
        value += l2[i].val
        value += carry
        if value >= 10:
            carry = value//10
            value -=10
        output.append(value)
        i += 1
        value=0
    return output


x = addTwoNumbers(l_one, l_two)
print(x)
s=l_one.__len__()
print(s)