class Solution {
    public String lexGreaterPermutation(String s, String target) {
int n=s.length();
        int[] chars=new int[128];
        int MatchLen=0;
        for (int i=0;i<s.length();i++){
            chars[s.charAt(i)]++;
        }
        while(MatchLen<n && chars[target.charAt(MatchLen)]>0){
            chars[target.charAt(MatchLen)]--;
            MatchLen++;
        }
        for(int i=MatchLen;i>=0;i--){
            if (i<MatchLen){
                chars[target.charAt(i)]++;
            }
            if(i<n){
                char targetchar=target.charAt(i);
                for(int j=targetchar+1;j<='z';j++){
                    if(chars[j]>0){
                        StringBuilder res =new StringBuilder();
                        res.append(target.substring(0,i));
                        res.append((char) j);
                        chars[j]--;
                        for(int t=0;t<chars.length;t++){
                            while(chars[t]>0){
                                res.append((char) t);
                                chars[t]--;
                            }
                        }
                        return res.toString();
                    }
                }
                
            }
        }
        return "";

    }
       
}