class Solution {
    public int missingMultiple(int[] nums, int k) {
        Set<Integer> set=new HashSet<>();
        for(int num: nums){
            set.add(num);
        }
        for(int i=1;i<nums.length+1;i++){
            if (set.contains(i*k)){continue;}
            else{
                return i*k;
            }
        }
        return (nums.length+1)*k;
    }
}