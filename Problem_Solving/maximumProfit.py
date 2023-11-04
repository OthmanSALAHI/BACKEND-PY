        

class Solution(object):
    def maxPrice(self, prices):
            if not prices:
                return 0
            max_price = prices[0]
            for price in prices:
                if price > max_price:
                    max_price = price
            return max_price
    def minPrice(self, prices):
            if not prices:
                return 0
            min_price = prices[0]
            for price in prices:
                if price < min_price:
                    min_price = price
            return min_price
    def minimum(self,curr,prev):
        if curr < prev:
            prev = curr
        return prev

    def maxprofit(self,prices):
        if not prices:
            return None

        maxProfit = 0
        mini = prices[0]
        for price in prices:
            mini = self.minimum(price,mini)
            maxProfit = max(maxProfit , price - mini)
        return maxProfit

def main():
    week = [9,9,9,9,1,4]
    solution = Solution()

    profit = solution.maxprofit(week)
    maxPrice = solution.maxPrice(week)
    minPrice = solution.minPrice(week)

    print(f"the max is {maxPrice}, the min price is {minPrice}, the maximum profit is {profit}")

if __name__ == "__main__":
    main()