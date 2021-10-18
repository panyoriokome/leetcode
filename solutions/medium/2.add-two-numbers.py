#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
from typing import Optional, List

ListNode = List[int]

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # JoinとReverseどっちを先にするのが効率的？
        # Reverseする
        l1_reverse = reversed(l1)
        l2_reverse = reversed(l2)
        # Joinする
        l1_join = ''.join([str(n) for n in l1_reverse])
        l2_join = ''.join([str(n) for n in l2_reverse])

        # intにする
        result = int(l1_join) + int(l2_join)

        return result

s = Solution()
print(s.addTwoNumbers([2,4,3], [5,6,4]))

# @lc code=end

