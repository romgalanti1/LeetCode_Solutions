class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # a letter can participate in a palindrome if it appears over 2 times in s
        # middle letter in palindrome can appear once
        # use counter s to find the num of letters that can participate in palindrome

        length = 0
        cntr = Counter(s)
        for letter in cntr.keys():
            while cntr[letter] > 1:
                length += 2
                cntr[letter] -= 2
                if cntr[letter] == 0:
                    del cntr[letter]
        if cntr:
            length += 1
        
        return length
