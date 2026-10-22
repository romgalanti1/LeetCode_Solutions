class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        char_to_num = []
        for char in s:
            if char_to_num and char_to_num[-1][0] == char:
                char_to_num[-1][1] += 1
            else:
                char_to_num.append([char,1])
        n = len(char_to_num)

        def isStretchy(word):
            c_t_n = []
            for char in word:
                if c_t_n and c_t_n[-1][0] == char:
                    c_t_n[-1][1] += 1
                else:
                    c_t_n.append([char,1])
            if len(c_t_n) != n:
                return False
            else:
                for i in range(n):
                    w,s = c_t_n[i][0], char_to_num[i][0]
                    cw, cs = c_t_n[i][1], char_to_num[i][1]
                    if w != s or cw > cs or (cw < cs and cs < 3):
                        return False
            return True

        Stretchy_Count = 0
        for word in words:
            if isStretchy(word):
                Stretchy_Count += 1
        return Stretchy_Count