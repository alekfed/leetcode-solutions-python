class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        list_str = list(s.strip())
        if not list_str:
            return 0

        if list_str[0] == '-':
            sign = -1
        else:
            sign = 1

        if list_str[0] in ['-', '+']:
            del list_str[0]

        ret, i = 0, 0

        while i < len(list_str) and list_str[i].isdigit():
            ret = ret*10 + ord(list_str[i]) - ord('0')
            i += 1

        return max(-2**31, min(sign * ret, 2**31-1))
