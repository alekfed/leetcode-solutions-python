class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for i in range(len(haystack)-len(needle)+1):
            for j, cur_needle in enumerate(needle):
                if haystack[i+j] != cur_needle:
                    break
                if j == len(needle) - 1:
                    return i

        return -1
