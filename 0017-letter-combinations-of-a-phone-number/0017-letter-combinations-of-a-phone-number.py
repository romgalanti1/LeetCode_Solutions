class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_to_letter = {"2" : ["a","b","c"],
        '3':["d","e","f"],
        '4':["g","h","i"],
        '5':["j","k","l"],
        '6':["m","n","o"],
        '7':["p","q","r","s"],
        '8':["t","u","v"],
        '9':["w","x","y","z"]}

        output = []
        n = len(digits)
        # recurse through digits while building the string
        def recBuild(s,i):
            if i == n:
                output.append(s)
                return
            for character in num_to_letter[digits[i]]:
                recBuild(s + character, i + 1)
            return
        
        recBuild("",0)

        return output