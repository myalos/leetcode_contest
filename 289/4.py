from typing import *

# solution/by-endlesscheng-92fw
class Solution:
    def longestPath(self, parent : List[int], s : str) -> int:
        # 感觉这道题意比较简单，但是要花点时间想一下
        # 将parent转成树的邻接表
        adjlist = [[] for _ in range(len(parent))]
        for i in range(1, len(parent)):
            adjlist[parent[i]].append(i)
        # dp[i] 表示以i为根结点的树中根结点起始的最长路径为dp[i]
        ans = 0
        def dfs(x):
            nonlocal ans
            max_len = 0
            for y in adjlist[x]:
                len = dfs(y) + 1 #一个结点只会被dfs一次，调用者是其父节点，父节点只有一个
                if s[y] != s[x]:
                    # 在考虑y结点时，max_len是之前遍历过的x的子结点中得到的从x出发的最大路径
                    ans = max(ans, max_len + len + 1)
                    max_len = max(max_len, len)
            return max_len
        dfs(0)
        return ans

# 下面的是一种错误写法
class Solution1:
    def longestPath(self, parent : List[int], s : int) -> int:
        adjlist = [[] for _ in range(len(parent))]
        for i in range(1, len(parent)):
            adjlist[parent[i]].append(i)
        ans = 1
        def dfs(x):
            nonlocal ans
            max_len = 0
            for y in adjlist[x]:
                # 当s[x] == s[y]就把这个分支给断掉了，这样不合适，如果最长路径存在于这个分支里面，那么就会出问题，不管是否相等，分支还是要进行dfs的
                if s[x] == s[y]:
                    continue
                len = dfs(y) + 1
                ans = max(ans, len + max_len + 1)
                max_len = max(max_len, len)
            return max_len
        dfs(0)
        return ans


def main():
    sol = Solution()
    _input = ([-1, 0, 0, 1, 1, 2], "abacbe")
    _output = sol.mya(*_input)
    print(_output)

if __name__ == '__main__':
    main()
