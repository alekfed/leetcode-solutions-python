from collections import deque, defaultdict, Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words:
            word_len = len(words[0])
        else:
            word_len = 0
        s_len = len(s)
        word_len_total = len(words) * word_len
        count = Counter(words)
        footprint = defaultdict(deque)
        result = []

        for start in range(word_len):
            footprint.clear()
            end = start
            while start + word_len_total <= s_len:
                sub = s[end:end+word_len]
                end += word_len
                if sub in count:
                    queue = footprint[sub]
                    queue.append(end)
                    while queue[0] < start:
                        queue.popleft()
                    if len(queue) > count[sub]:
                        start = queue.popleft()
                    if start + word_len_total == end:
                        result.append(start)
                else:
                    start = end

        return result
