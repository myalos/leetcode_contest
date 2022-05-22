# 二维数组 stockPrices stockPrices[i] = day[i], price[i] 表示股票在dayi 的价格为prices，这个画出来的图是一个折线图，求折线图线段的个数
from typing import *

class Solution:
    def minimumLines(self, stockPrices : List[List[int]]) -> int:
        if len(stockPrices) <= 2: return len(stockPrices) - 1
        from collections import namedtuple
        Grad = namedtuple('Grad', ['day', 'price'])
        stockPrices.sort(key = lambda x : x[0])
        ans, grad = 1, Grad(day = stockPrices[1][0] - stockPrices[0][0], price = stockPrices[1][1] - stockPrices[0][1])
        for i in range(1, len(stockPrices) - 1):
            day1, price1 = stockPrices[i]
            day2, price2 = stockPrices[i + 1]
            if (day2 - day1) * grad.price != grad.day * (price2 - price1):
                ans += 1
            grad = Grad(day = day2 - day1, price = price2 - price1)
        return ans

def main():
    sol = Solution()
    _input = ([[3, 4], [1, 2], [7, 8], [2, 3]], )
    _output = sol.minimumLines(*_input)
    print(_output)

if __name__ == '__main__':
    main()
