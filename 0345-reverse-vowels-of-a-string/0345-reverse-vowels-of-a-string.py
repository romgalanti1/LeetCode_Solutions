class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        vowels={'a','A','e','E','i','I','o','O','u','U'}
        if not s:
            return ""
        arr=list(s)
        i=0
        j=n-1
        while i<j:
            while arr[i] not in vowels and i<j:
                i+=1
            while arr[j] not in vowels and j>i:
                j-=1
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            i+=1
            j-=1
        return "".join(arr)