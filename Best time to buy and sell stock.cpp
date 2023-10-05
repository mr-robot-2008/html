//using dynamic programming
int maxProfit(vector<int>&prices){
	int n= prices.size();
	int curr_sell = prices[0];
	int profit =0;
	
	for(int i=1;i<n;i++){
		profit = max(profit,prices[i]-curr_sell);
		curr_sell = min(curr_sell,prices[i]);
		
	}
	return profit;
}