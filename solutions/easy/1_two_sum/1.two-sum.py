#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
import itertools

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        combinations = itertools.combinations(nums, 2)
        for i in combinations:
            if i[0] + i[1] == target:
                fisrt_index = nums.index(i[0])
                second_index = nums.index(i[1])
                indices = [fisrt_index, second_index]
                break

        return indices

# @lc code=end

