from collections import defaultdict


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        nexts = 1
        end_bit = 1 << len(s)
        int_dict = defaultdict(int)

        for i, char in enumerate(s):
            int_dict[char] |= 1 << i

        for char in p:
            if char == '*':
                nexts = (end_bit << 1) - (nexts & -nexts)
            elif char == '?':
                nexts <<= 1
            else:
                nexts = (nexts & int_dict[char]) << 1
            if nexts == 0:
                return False

        return nexts & end_bit != 0
