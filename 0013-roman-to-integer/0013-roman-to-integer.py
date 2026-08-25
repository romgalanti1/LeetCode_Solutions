class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        ans = my_map[s[0]]

        for i in range(1,len(s)):
            if(my_map[s[i]] > my_map[s[i-1]]):
                ans += my_map[s[i]]
                ans -= 2 * my_map[s[i-1]]
            else:
                ans += my_map[s[i]]        

        return ans