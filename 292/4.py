from typing import *

# 一个括号字符串是一个非空且只包含'('和')'的字符串，如果下面任意条件为真，那么这个括号字符串就是合法的：
#    字符串是()
#    字符串可以表示为AB, A和B都是合法的
#    字符串可以表示为(A), 其中A是合法括号序列
#    m x n的括号网格图矩阵 grid, 网格图中一个合法括号路径是满足一下所有条件的一条路径：
#    路径开始(0, 0)
#    路径结束 (m - 1, n - 1) 右下角的格子
#    路径每次只会向下或者向右移动
#    路径经过的格子组成的括号字符串是合法的
#    如果网络中存在一条括号合法路径就返回true

# 代码参考自灵茶山艾府的解析
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        # dfs返回在位置(x, y) 有c个括号
        # 我之前的代码是在(x, y)的位置上面配置了一个set，这个set里面装了到x,y所有的可能，艾神的方法 是dp方法，x,y,c来判断到达位置x, y的时候左括号堆积了c个，我的代码考虑每一种情况是装进set里面的，而这边的方法是通过or操作
        from functools import lru_cache
        # 艾神 用的是cache 文档里面说这个是3.9开始的函数，返回值与lru_cache(maxsize = None)相同
        m, n = len(grid), len(grid[0])
        # 从艾神的代码中，我发现括号必须要成对，不管是怎么一个路线，经过的括号总数是m + n - 1 所以m + n - 1要是偶数
        if grid[0][0] == ')' or grid[-1][-1] == '(' or (m + n) % 2 == 0:
            return False
        @lru_cache(maxsize=None)
        def dfs(x, y, c):
            # 剩余的括号不足以消掉c个括号
            if (m - x) + (n - y) - 1 < c:
                return False
            # 边界条件
            if x == m - 1 and y == n - 1: return c == 1
            if grid[x][y] == '(':
                c += 1
            else:
                c -= 1
            if c < 0:
                return False
            # 下面这个写法可以的
            return x < m - 1 and dfs(x + 1, y, c) or y < n - 1 and dfs(x, y + 1, c)
        return dfs(0, 0, 0)

def main():
    sol = Solution()
    _input = ([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]], )
    _output = sol.hasValidPath(*_input)
    print(_output)

if __name__ == '__main__':
    main()
