class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # sort each string, find its bucket index and append to bucket
        # keep dictionary of string-> bucket indx
        
        output = []
        string_to_bucket = {}
        
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in string_to_bucket:
                output.append([])
                string_to_bucket[sorted_string] = len(output) - 1
            output[string_to_bucket[sorted_string]].append(string)
        return output
                