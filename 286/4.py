from typing import *

# 题目数据有个重要的条件就是  k <= sum(piles[i].length) <= 2000
# _input1 = ([[48, 14, 23, 38, 33, 79, 3, 52, 73, 58, 49, 23, 74, 44, 69, 76, 83, 41, 46, 32, 28]], 10)
# WA 对于上面的数据 就会出问题
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k : int) -> int:
        # 分组背包
        # dp[i][j] 表示 从前i个栈 进行了k次操作 钱包里硬币面值之和最大值为多少
        # dp[i][j] = max(dp[i - 1][j - m] + sum(piles[i][0 ... m - 1]))
        # 其中 0 <= m <= min(len(piles[i]), j)
        n, _n = len(piles), 0 # _n 里面记录的是前i个栈最多可以进行的操作
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, 1 + n): # 从1到n 表示n个堆
            _n += len(piles[i - 1])
            for j in range(1, len(piles[i - 1])):
                piles[i - 1][j] += piles[i - 1][j - 1]
            # 索引的应用就比较繁琐
            for j in range(1, 1 + min(_n, k)):
                dp[i][j] = max(dp[i - 1][j], *[dp[i - 1][j - m - 1] + piles[i - 1][m] for m in range(min(len(piles[i - 1]), j))])
        return dp[n][k]

# 错误原因是dp数组的维度开错了
# 前面的是列 后面的是行
class Solution1:
    def maxValueOfCoins(self, piles: List[List[int]], k : int) -> int:
        n, _n = len(piles), 0 # _n 里面记录的是前i个栈最多可以进行的操作
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, 1 + n): # 从1到n 表示n个堆
            _n += len(piles[i - 1])
            for j in range(1, len(piles[i - 1])):
                piles[i - 1][j] += piles[i - 1][j - 1]
            # 索引的应用就比较繁琐
            for j in range(1, 1 + min(_n, k)):
                dp[i][j] = max(dp[i - 1][j], *[dp[i - 1][j - m - 1] + piles[i - 1][m] for m in range(min(len(piles[i - 1]), j))])
        return dp[n][k]

def main():
    sol = Solution1()
    _input = ([[1, 100, 3], [7, 8, 9]], 2)
    _input1 = ([[48, 14, 23, 38, 33, 79, 3, 52, 73, 58, 49, 23, 74, 44, 69, 76, 83, 41, 46, 32, 28]], 10)
    _output = sol.maxValueOfCoins(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
