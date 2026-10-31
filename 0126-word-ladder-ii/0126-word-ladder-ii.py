class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # bfs to find shortest paths while keeping parent list
        # dfs from endword back to beginword with parent pointers
        #
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        output = []
        parents = defaultdict(list) # childword -> list of parent words
        q = deque([(beginWord,0)])
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        distances = {beginWord:0} # word -> distance from beginword
        
        while q:
            curr, distance = q.popleft()
            if curr == endWord:
                break
            # find neighbors
            for i in range(len(curr)):
                for c in alphabet:
                    candidate = curr[:i] + c + curr[i + 1:]
                    if candidate in wordSet: # valid neighbor
                        if candidate in distances and distances[candidate] == distance + 1:
                            parents[candidate].append(curr)
                        elif candidate not in distances:
                            distances[candidate] = distance + 1
                            q.append((candidate,distance + 1))
                            parents[candidate].append(curr)
        # now dfs from endword to beginword while appending path to output
        
        def dfs(word,path):
            if word == beginWord:
                output.append(path[::-1])
                return
            
            for parent in parents[word]:
                dfs(parent,path + [parent])
            
        
        dfs(endWord,[endWord])
        return output
                
                            
                            
                        
                        
            
        
        