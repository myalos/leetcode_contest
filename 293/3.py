# 选nums数组中若干个数，进行与操作，如果结果大于0就是一个合格的选择，求数量最大的合格的选择
from typing import *

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        weight = [2 ** i for i in range(24)]
        ans = [0] * 24
        for num in candidates:
            for j in range(24):
                if num & weight[j] > 0:
                    ans[j] += 1
        return max(ans)


def main():
    sol = Solution()
    _input = ([16, 17, 71, 62, 12, 24, 14], )
    _input1 = ([8, 8], )
    _output = sol.largestCombination(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
