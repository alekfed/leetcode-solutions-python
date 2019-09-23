class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for index, elem in enumerate(digits):
            num += elem * pow(10, (len(digits) - 1 - index))
        return [int(i) for i in str(num + 1)]
