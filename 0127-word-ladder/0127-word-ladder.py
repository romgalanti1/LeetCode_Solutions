class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # bfs from beginword to endword and return number of steps.
        # each neighbor is 1 letter from word
        # keep visited set
        # dynamically find neighbors in wordList
        
        wordset = set(wordList)
        q = deque([(beginWord,1)])
        visited = set()
        n = len(beginWord)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        while q:
            curr_word, steps = q.popleft()
            if curr_word == endWord:
                return steps
            
            for i in range(n):
                for c in alphabet:
                    candidate = curr_word[:i] + c + curr_word[i + 1:]
                    if candidate in wordset and candidate not in visited:
                        q.append((candidate,steps + 1))
                        visited.add(candidate)
        return 0
                    
                    
                