# 0到n-1的n个背包 给你两个下标从0开始的整数数组
# capacity和rocks 第i个背包最大可以装capacity[i]块石头，当前已经装了rocks[i]块石头。另外一个additionalRocks 表示可以放置的额外石头的数量 石头可以往任意背包中放置
# 将额外的石头放入一些背包中，并返回放置后装满石头的背包的最大数量
from typing import *

class Solution:
    def maximumBags(self, capacity : List[int], rocks : List[int], additionalRocks : int) -> int:
        remain = map(lambda i : capacity[i] - rocks[i], range(len(rocks)))
        remain = list(sorted(remain))
        ans = 0
        for i in range(len(remain)):
            _min = min(remain[i], additionalRocks)
            remain[i] -= _min
            additionalRocks -= _min
            if remain[i] == 0:
                ans += 1
            else:
                break
        return ans


def main():
    sol = Solution()
    _input = ([2, 3, 4, 5], [1, 2, 4, 4], 2)
    _output = sol.maximumBags(*_input)
    print(_output)

if __name__ == '__main__':
    main()
