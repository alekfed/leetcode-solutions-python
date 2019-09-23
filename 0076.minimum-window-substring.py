class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1

        to_find, ind = len(t), []
        left, right, head = -len(s) - 1, -1, 0

        for i, c in enumerate(s):
            if c in d:
                ind.append(i)
                d[c] -= 1
                if d[c] >= 0:
                    to_find -= 1
                if to_find == 0:
                    while d[s[ind[head]]] < 0:  # s[ind[head]] is the character
                        d[s[ind[head]]] += 1
                        head += 1
                    if i - ind[head] < right - left:
                        left, right = ind[head], i

                    d[s[ind[head]]] += 1
                    to_find += 1
                    head += 1

        return s[left:right+1]
