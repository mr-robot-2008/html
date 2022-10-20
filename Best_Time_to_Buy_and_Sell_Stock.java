class Solution {
    public int maxProfit(int[] prices) {
        
        //Brute Force : --> Time Limit Exceeding
      
        // int profit = Integer.MIN_VALUE;
        // for (int i=0;i<prices.length;i++){
        //     for(int j=i+1;j<prices.length;j++){
        //         if ((prices[j]-prices[i])>profit)
        //             profit=prices[j]-prices[i];
        //     }
        // }
        // if (profit<0) return 0;
        // return profit;
        
        //One -Pointer Appraoch  +  O(n)
        
//          int buy = Integer.MAX_VALUE;
//          int profit = 0;
        
//         for(int i=0; i < prices.length; i++){
            
//             if(prices[i] < buy)     buy = prices[i];
            
//             profit = Math.max(profit, prices[i] - buy);         //sell = prices[i] - buy;
//         }
//         return profit;
        
        //Approach 02
        
        
        
        int buy =Integer.MAX_VALUE, max=0;
        
        for (int i=0;i<prices.length;i++){
            
            if(buy>prices[i])   buy = prices[i];
            max= Math.max(max, prices[i]-buy);
        }
        return max;
        
        
        
    }
}


// Input: prices = [7,1,5,3,6,4]
// Output: 5
