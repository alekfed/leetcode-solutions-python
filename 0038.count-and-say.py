class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dic = {}
        dic[0] = "1"

        for i in range(n):
            if i not in dic:
                phrase = dic[i-1]

                count = 0
                cur_int = phrase[0]
                new_phrase = ""
                for c in phrase:
                    if c == cur_int:
                        count += 1
                    else:
                        new_phrase += str(count) + str(cur_int)
                        count = 1
                        cur_int = c

                new_phrase += (str(count) + str(cur_int))

                dic[i] = new_phrase

        return dic[n-1]
