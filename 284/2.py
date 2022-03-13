from typing  import *

# artifacts和dig的长度可以达到10^5 所以暴力是不行的
# 我可以把dig 变成二维数组 然后对于每个artifacts 在二维数组里面进行查询
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # 将dig 变成二维数组flag，flag[i][j]表示第i,j的位置是否被挖
        flag = [[0] * n for _ in range(n)]
        ans = 0
        for x, y in dig:
            flag[x][y] = 1
        for r1, c1, r2, c2 in artifacts:
            flag2 = 1 # flag2 当前的artifact是否可以被提取
            x, y = r1, c1
            # 检查这个artifact所有的位置是否被挖
            while x <= r2:
                while y <= c2:
                    if flag[x][y] == 0:
                        flag2 = 0
                    y += 1
                x += 1
                y = c1
            if flag2:
                ans += 1
        return ans


        

def main():
    sol = Solution()
    _input = (2, [[0,0,0,0],[0,1,1,1]], [[0,0],[0,1]])
    _input1 = (2, [[0,0,0,0],[0,1,1,1]], [[0,0],[0,1],[1,1]])
    _output = sol.digArtifacts(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
