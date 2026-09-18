class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int min=1;int max=0;
        for(int i:piles) {
            if(i>max) max=i;
        }
        int ans=max;
        while(min<=max) {
            long cnt=0;
            int mid=min+(max-min)/2;
            for(int i:piles) {
                cnt += (i + mid - 1) / mid; 
            }
            if (cnt <= h) {
                ans = mid;
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }
        return ans;
    }
}