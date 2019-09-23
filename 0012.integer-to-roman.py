class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        arabic_to_roman_map = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        ans = ''

        for k in sorted(arabic_to_roman_map, reverse=True):
            quotient = num//k
            if quotient != 0:
                ans += arabic_to_roman_map[k] * quotient
                num -= quotient*k

        return ans
