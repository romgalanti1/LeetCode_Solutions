from collections import Counter
class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n=len(s)
        res=""
        middlechar=""
        counts=Counter(s)
        for char in counts:
            if counts[char] % 2 != 0 and middlechar=="":
                middlechar=char
            elif counts[char] % 2 !=0:
                return ""
        halfcounts={char:counts[char]//2 for char in counts}
        half_n=n//2
        match_len=0
        for i in range (half_n):
            if(halfcounts.get(target[i],0)>0):
             res+=target[i]
             halfcounts[target[i]]-=1
             match_len+=1
            else:
                break
        if match_len==half_n:
            candidate=target[:half_n]+middlechar+target[:half_n][::-1]
            if candidate>target:
                return candidate
        for i in range(match_len,-1,-1):
            if (i<match_len):
                halfcounts[target[i]]+=1
            if (i<half_n):
              target_char=target[i]
              for j_code in range(ord(target_char)+1,ord('z')+1):
                  j_char=chr(j_code)
                  if (halfcounts.get(j_char,0)>0):
                      halfcounts[j_char]-=1
                      res=target[:i]+j_char
                      res_second_half="".join(sorted([char for char,cnt in halfcounts.items() for s in range(cnt)]))
                      first_half=res+res_second_half
                      full_palindrome=first_half+middlechar+first_half[::-1]
                      return full_palindrome
        return ""                   


        