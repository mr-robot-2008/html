class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxi=0; // for returning the answer
        int n =height.size();

        //why left 0 and right n-1 ->we want width to be maximum
        int left =0;
        int right=n-1;
        while(left<right){
            int w=right-left;
            int h=min(height[left],height[right]);
            int area= w * h;
            maxi=max(maxi,area);

            if(height[left]<height[right])left++;//shifting left pointer to right
            else if (height[left]>height[right])right--;//shifting right pointer to left
            else{
                left++;
                right--;
            }
        }
        return maxi;
        
    }
};