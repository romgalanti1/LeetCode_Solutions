class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. ignore leading spaces -> check at start
        # 2. check signness -> keep in flag at the end check isPositive = True
        # 3. check the range

        isPositive = True
        n = len(s)
        i = 0

        # step 1 ignore spaces
        while i < n and s[i] == " ":
            i += 1
        
        # step 2 check sign
        if i < n and s[i] == "-":
            isPositive = False
            i += 1
        elif i < n and s[i] == "+":
            i += 1
        
        # step 3 build the number digit by digit
        num = 0
        while i < n and s[i].isdigit():
            num *= 10
            num += ord(s[i]) - ord("0")
            i += 1
        

        # check range
        if num >= 2 ** 31 and isPositive:
            num = (2 ** 31) - 1
        elif num > 2 ** 31 and not isPositive:
            num = 2 ** 31
        
        # check sign
        if not isPositive:
            num = -num
        
        

        return num
        