class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match_hash = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in match_hash:
                if not (stack and stack.pop() == match_hash[char]):
                    return False
            else:
                stack.append(char)

        return not stack
