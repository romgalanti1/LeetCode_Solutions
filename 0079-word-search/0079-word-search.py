class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited=set()
        if not board:
            return False
        n=len(board)
        m=len(board[0])
        length=len(word)
        first_letter_pos=[]
        for row in range(n):
            for col in range(m):
                if board[row][col]==word[0]:
                    first_letter_pos.append((row,col))
        def dfs(r,c,i,visited):
            if i==len(word):
                return True
            if r>=n or c>=m or c<0 or r<0:
                return False
            if board[r][c]!=word[i]:
                return False
            if (r,c) in visited:
                return False
            visited.add((r,c))
            check_up=dfs(r-1,c,i+1,visited)
            check_down=dfs(r+1,c,i+1,visited)
            check_right=dfs(r,c+1,i+1,visited)
            check_left=dfs(r,c-1,i+1,visited)
            visited.remove((r,c))
            return check_up or check_down or check_right or check_left
        for pos in first_letter_pos:
            r=pos[0]
            c=pos[1]
            if dfs(r,c,0,visited):
                return True
        return False
            

