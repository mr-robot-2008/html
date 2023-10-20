class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int>temp;
        temp.push_back(nums[0]);
        int len=1;

        for(int i=0;i<nums.size();i++){
            if(nums[i]>temp.back()){
                temp.push_back(nums[i]);
                len++;
            }
            else{
                int index=lower_bound(temp.begin(),temp.end(),nums[i])-temp.begin();
                temp[index]=nums[i];
            }
        }

        return len;
    }
};
