class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        output = []
        for s in strs:
            k = len(s)
            output.append(str(k) + "#" + s)
        return "".join(output)

        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        output = []
        i = 0 
        n = len(s)


        3#
        while i < n:
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            if i < n and s[i] == "#":
                word = s[i + 1: i + 1 + num]
                output.append(word)
                i = i + 1 + num

        return output 
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))