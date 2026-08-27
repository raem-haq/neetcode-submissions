class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def res(coins, t, memo={}):
            if t < 0:
                return float('inf')
            if t == 0:
                return 0
            if t in memo:
                return memo[t]
            
            m = float('inf')
            for coin in coins:
                if coin <= t:
                    m = min(m, 1 + res(coins, t - coin, memo))
            memo[t] = m
            return m
        
        ans = res(coins, amount) 
        if ans == float('inf'):
            return -1
        return ans