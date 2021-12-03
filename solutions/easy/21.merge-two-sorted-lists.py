#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = list.extend(list)
        print(merged)

list1 = [1,2,4]
list2 = [1,3,4]
Solution().mergeTwoLists(list1, list2)

ListNode(3, )
        
# @lc code=end

