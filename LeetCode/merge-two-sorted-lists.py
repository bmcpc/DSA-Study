# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
create a new pointer to merged list using dummy node
create curr pointer to iterate through merged list

"""


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # use dummy node so that we can simplify code to within loop
        head = ListNode(0)
        curr = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next

        # append whichever list is still not iterated completely
        curr.next = list1 if list1 is not None else list2
        return head.next
