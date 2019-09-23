class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length_s = len(s)

        if length_s <= 1:
            return s

        start, i = 0, 0
        max_length = 1

        while i < length_s:
            if length_s - i <= max_length/2:
                break

            j, k = i, i

            while k < length_s - 1 and s[k] == s[k + 1]:
                k += 1

            i = k + 1

            while k < length_s - 1 and j and s[k + 1] == s[j - 1]:
                k, j = k + 1, j - 1

            if k - j + 1 > max_length:
                start, max_length = j, k - j + 1

        return s[start:start + max_length]
