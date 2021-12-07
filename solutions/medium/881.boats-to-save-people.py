#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # limit内でできるだけweightを消費できる人の組み合わせを見つける
        people.sort()
        left = 0
        right = len(people) -1
        boats_number = 0

        while(left <= right):
            if(left == right):
                boats_number+=1
                break

            if(people[left]+people[right] <= limit):
                left+=1

            right-=1
            boats_number += 1
        return boats_number

        
# @lc code=end

