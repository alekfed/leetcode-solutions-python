class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        rev_num1 = num1[::-1]
        rev_num2 = num2[::-1]
        sum1, sum2 = 0, 0

        for i, elem in enumerate(rev_num1):
            sum1 += num_dict[elem] * 10**i

        for i, elem in enumerate(rev_num2):
            sum2 += num_dict[elem] * 10**i

        return str(sum1 * sum2)
