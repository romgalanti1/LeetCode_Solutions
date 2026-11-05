class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # ransom note can be constructed from magazine if each letter in ransomnote is in magazine
        # approach -> count letters in magazine in dictionary
        # for each letter in ransomnote lower count by one, if count is 0 delete it
        
        counter = Counter(magazine)

        for c in ransomNote:
            if c not in counter:
                return False
            
            else:
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
        
        return True

        