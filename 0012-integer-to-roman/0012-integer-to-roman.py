class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Int_to_Roman = {1 : "I",
                        4 : "IV",
                        5 : "V",
                        9 : "IX",
                        10 : "X",
                        40 : "XL",
                        50 : "L",
                        90 : "XC",
                        100 : "C",
                        400 : "CD",
                        500 : "D",
                        900 : "CM",
                        1000 : "M",}
        keys_sorted = sorted(Int_to_Roman.keys())
        def findmaxtosubtract(num):
            num_to_return = 0
            for sub in keys_sorted:
                if sub <= num:
                    num_to_return = sub
                    
            return num_to_return
               
        output = []
        while num > 0:
            num_to_subtract = findmaxtosubtract(num)
            output.append(Int_to_Roman[num_to_subtract])
            num -= num_to_subtract
        return "".join(output)
            