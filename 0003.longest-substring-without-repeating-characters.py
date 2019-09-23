class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        longest_str = s[0]
        longest_len = 1

        for letter in s[1:]:
            if letter in longest_str:
                i = longest_str.find(letter)
                longest_str = longest_str[i+1:]
            longest_str += letter
            if len(longest_str) > longest_len:
                longest_len = len(longest_str)

        return longest_len
