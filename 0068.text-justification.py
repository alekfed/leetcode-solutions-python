class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []

        cur_words = [words[0]]
        cur_len = len(words[0])

        for word in words[1:]:
            if cur_len + len(word) + 1 > maxWidth:
                ans.append(self.constr_str(cur_words, cur_len, maxWidth))
                cur_words = [word]
                cur_len = len(word)
            else:
                cur_words.append(word)
                cur_len += len(word) + 1

        ans.append(self.constr_str(cur_words, cur_len, maxWidth, True))

        return ans

    @staticmethod
    def constr_str(words, cur_len, max_width, last=False):
        """Construct string."""
        if len(words) == 1 or last:
            string = " ".join(words)
            string += " " * (max_width - len(string))
        else:
            word_len = cur_len - len(words) + 1
            space = max_width - word_len
            space_width = space // (len(words) - 1)
            space_res = space % (len(words) - 1)
            string = ""

            for i, word in enumerate(words):
                string += word
                if i < len(words) - 1:
                    spaces = space_width
                    if i < space_res:
                        spaces += space_res > 0
                    string += " " * spaces

        return string
