class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # start from lsb to msb while keeping a carry
        # if 1,1 -> carry is 1 res is 0 , if 0,1 res is 1 carry 0
        # add with two pointers and check the rest
        n = len(a)
        m = len(b)
        carry = 0
        res = []
        i = n - 1
        j = m - 1
        1010
        1011
        [1,0]
        while i >= 0 or j >= 0:
            a_bit = a[i] if i >= 0 else "0"
            b_bit = b[j] if j >= 0 else "0"
            if a_bit == "1" and b_bit == "1" and carry == 1:
                res.append("1")
                carry = 1
            elif a_bit == "1" and b_bit == "1":
                res.append("0")
                carry = 1
            elif (a_bit == "1" or b_bit == "1") and carry == 1:
                res.append("0")
                carry = 1
            elif a_bit == "1" or b_bit == "1":
                res.append("1")
            elif carry == 1:
                res.append("1")
                carry = 0
            else:
                res.append("0")
            i -= 1
            j -= 1
        
        if carry == 1:
            res.append("1")
        
        return "".join(res[::-1])
        
        


        