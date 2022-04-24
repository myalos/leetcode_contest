from typing import *

class Solution:
    def maxTrailingZeros(self ,grid : List[List[int]]) -> int:
        # 计算num的质因子2和质因子5的指数
        def process(num):
            save = num
            twofive = [0, 0]
            mapping = {0: 2, 1: 5}
            for i in range(2):
                num = save
                while (num % mapping[i] == 0):
                    num //= mapping[i]
                    twofive[i] += 1
            return twofive
        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = process(grid[i][j])
        # 我这个多维数组初始化相当的笨重
        rows = [[None ] * (n + 1) for _ in range(m)]
        cols = [[None ] * (m + 1) for _ in range(n)]
        for i in range(m):
            for j in range(n + 1):
                rows[i][j] = [0, 0]
                if j > 0:
                    rows[i][j][0] = rows[i][j - 1][0] + grid[i][j - 1][0]
                    rows[i][j][1] = rows[i][j - 1][1] + grid[i][j - 1][1]

        for i in range(n):
            for j in range(m + 1):
                cols[i][j] = [0, 0]
                if j > 0:
                    cols[i][j][0] = cols[i][j - 1][0] + grid[j - 1][i][0]
                    cols[i][j][1] = cols[i][j - 1][1] + grid[j - 1][i][1]

        # 遍历每个转角
        for i in range(m):
            for j in range(n):
                # 左上 左包含转角
                ans = max(ans,min(rows[i][j + 1][0] + cols[j][i][0], rows[i][j + 1][1] + cols[j][i][1]))
                # 左下 左包含转角
                ans = max(ans, min(rows[i][j + 1][0] + cols[j][m][0] - cols[j][i + 1][0], rows[i][j + 1][1] + cols[j][m][1] - cols[j][i + 1][1]))
                # 右下 右包含转角
                ans = max(ans,min(rows[i][n][0] - rows[i][j][0] + cols[j][m][0] - cols[j][i + 1][0], rows[i][n][1] - rows[i][j][1] + cols[j][m][1] - cols[j][i + 1][1]))
                # 右上 右包含转角
                ans = max(ans, min(rows[i][n][0] - rows[i][j][0] + cols[j][i][0], rows[i][n][1] - rows[i][j][1] + cols[j][i][1]))
        return ans

def main():
    sol = Solution()
    _input = ([[4, 3, 2], [7, 6, 1], [8, 8, 8]], )
    _input1 = ([[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]], )
    _output = sol.maxTrailingZeros(*_input)
    print(_output)

if __name__ == '__main__':
    main()
