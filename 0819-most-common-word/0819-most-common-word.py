class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        #build words
        n = len(paragraph)
        words = []
        curr_word = []
        splits = set([" ",".","!","?","'",",",";"])
        for i in range(n):
            if paragraph[i] in splits:
                if curr_word:
                    words.append("".join(curr_word))
                    curr_word = []
            else:
                curr_word.append(paragraph[i].lower())
    
        if curr_word:
            words.append("".join(curr_word))
        
        
        ctr = Counter(words)
        heap = []
        
        for word,count in ctr.items():
            heapq.heappush(heap,(-count,word))
        
        banned = set(banned)
        while heap:
            _,candidate = heapq.heappop(heap)
            if candidate.lower() not in banned:
                return candidate.lower()