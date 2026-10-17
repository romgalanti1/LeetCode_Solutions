class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        #build graph:
        #double loop through the letters of each word in word
        #for each letter find the first different letter-> that letter is a neighbor
        adj = {c:set() for word in words for c in word}
        in_degree = {c:0 for c in adj}
        m = len(words)
        for i in range(m - 1):
            curr_word = words[i]
            next_word = words[i+1]
            if len(curr_word) > len(next_word) and curr_word.startswith(next_word):
                return ""
            for j in range(min(len(curr_word),len(next_word))):
                curr_letter = curr_word[j]
                next_letter = next_word[j]
                if curr_letter != next_letter:
                    if next_letter not in adj[curr_letter]:
                        adj[curr_letter].add(next_letter)
                        in_degree[next_letter] += 1
                    break
        res = []
        q = deque([c for c in in_degree if in_degree[c] == 0])
        while q:
            curr_char = q.popleft()
            res.append(curr_char)
            for neighbor in adj[curr_char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        if len(res) == len(in_degree):
            return "".join(res)
        return ""
       
        
        #bfs to find a cycle in the graph
        #if cycle found return ""
        # else return ordering 1,....,len(words)
        
        order = 0
        # go through first letters