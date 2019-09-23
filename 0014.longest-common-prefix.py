class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_zip, res = zip(*strs), ''

        for chars in str_zip:
            if len(set(chars)) > 1:
                break
            res += chars[0]

        return res
