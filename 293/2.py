# [bottom, top] 区间里面 去掉special里面的数字，求最大连续数字的个数
# 比如 [2, 9]里面去掉 (4, 6)那么最大的连续 就是7, 8, 9
from typing import *

class Solution:
    def maxConsecutive(self, bottom: int, top:int, special : List[int]) -> int:
        special.sort()
        ans = 0
        for cut in special:
            ans = max(ans, cut - bottom)
            # 之前bottom = cut 报错，错误原因是6被切了之后 剩余的是7 8 bottom应该是7 而不是6
            bottom = cut + 1
        return max(ans, top - cut)

def main():
    sol = Solution()
    _input = (6,8,[7,6,8])
    _input1 = (2, 9, [4 ,6])
    _output = sol.maxConsecutive(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
