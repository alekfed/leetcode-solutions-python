class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return_val = 0
        pair = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i, rom_num in enumerate(s):
            return_val += pair[rom_num]

            if i:
                if pair[s[i]] > pair[s[i-1]]:
                    return_val -= pair[s[i-1]] * 2

        return return_val
