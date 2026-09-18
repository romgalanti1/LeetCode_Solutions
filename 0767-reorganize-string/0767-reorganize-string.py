class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cntr=Counter(s)
        pq=[]
        res=[]
        n=len(s)
        for key,value in cntr.items():
            heapq.heappush(pq,(-value,key))
        prev_count,prev_char=0,""
        if -pq[0][0]> (n+1)//2:
            return ""
        while pq:
            count,char=heapq.heappop(pq)
            res.append(char)
            if prev_count<0:
                heapq.heappush(pq,(prev_count,prev_char))
            prev_count=count+1
            prev_char=char
        return "".join(res)