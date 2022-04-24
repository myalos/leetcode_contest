from typing import *

class Solution:
    def countLatticePoints(self, circles : List[List[int]]) -> int:
        # 一个圆对应一个点的集合，最终结果就是并集，我感觉这题暴力也能过
        ans = set()
        for x, y, r in circles:
            pt = set()
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                        pt.add((i, j))
            ans = ans | pt
        return len(ans)

def main():
    sol = Solution()
    _input = ([[2, 2, 1]], )
    _input1 = ([[2, 2, 2], [3, 4, 1]], )
    _output = sol.countLatticePoints(*_input)
    print(_output)

if __name__ == '__main__':
    main()
