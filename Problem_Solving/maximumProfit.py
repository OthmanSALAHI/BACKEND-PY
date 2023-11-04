"""def maxPrice(self, prices):
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
        return min_price"""
        

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

def main():
    week = [9,9,9,9,9,4]
    solution = Solution()

    profit = solution.maxProfit(week)
    maxPrice = solution.maxPrice(week)
    minPrice = solution.minPrice(week)

    print(f"the max is {maxPrice}, the min price is {minPrice}, the maximum profit is {profit}")

if __name__ == "__main__":
    main()