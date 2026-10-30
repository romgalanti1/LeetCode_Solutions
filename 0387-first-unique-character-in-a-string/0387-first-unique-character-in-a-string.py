class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # iterate from left to right
        # hold an array that stores each letter
        # hold a dictionary with letter -> index in the array
        # first time finding a duplicate change the value in array to 0
        # iterate through the letter array and return the first letter's index
        
        
        # leetcode -> [l,0,0,t,c,o,d,0]
        
        n = len(s)
        letter_to_index = [0 for _ in range(n)]
        seen = {}
        
        for i, char in enumerate(s):
            if char not in seen:
                letter_to_index[i] = char
                seen[char] = i
            else:
                letter_to_index[seen[char]] = 0
        
        for index in range(n):
            if letter_to_index[index] != 0:
                return index
        return -1