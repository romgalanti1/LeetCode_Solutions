class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
      String res="";
        int CountOnes=0;
        int left=0;
        int right=0;

        while(right<=s.length()-1){
            if(s.charAt(right)=='1'){
                CountOnes++;
            }
            while (CountOnes==k){
                while(s.charAt(left)=='0'){
                    left++;
                }
                String curr=s.substring(left,right+1);
                if(res==""){
                    res=curr;
                }
                else{
                     if(curr.length()<res.length() || ((curr.length()==res.length())&&(
                     curr.compareTo(res)<0))){
                    res=curr;
                }

                }
            
            left++;
            CountOnes--;
            }
            right++;
        }
            return res;

        }
    }
