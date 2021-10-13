#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 受け取った値を文字列に変換する
        x_str = str(x)

        # 文字列を逆転させる
        x_str_reversed = ''.join(reversed(x_str))

        result = False
        # 最初の値と一致しているか確認する
        if x_str == x_str_reversed:
            result = True
        else:
            result = False

        return result

# @lc code=end

