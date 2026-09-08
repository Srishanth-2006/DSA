class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n=nums.length;int left=1;int right=n-2;
        int mid=0;
        if (n == 1) return nums[0];
        if (nums[0] != nums[1]) return nums[0];
        if (nums[n - 1] != nums[n - 2]) return nums[n - 1];
        while(left<=right) {
            mid=left+(right-left)/2;
            if (nums[mid] != nums[mid - 1] && nums[mid] != nums[mid + 1]) {
                return nums[mid];
            }
            if ((mid % 2 == 0 && nums[mid] == nums[mid + 1]) ||
                (mid % 2 == 1 && nums[mid] == nums[mid - 1])) {
                left = mid + 1; // Step into right half
            } else {
                right = mid - 1; // Step into left half
            }
        }
        return -1;
    }
}