from typing import *

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 通过k来判断是否可以分 时间复杂度是O(n) 这题可以用二分来做
        # 因为这个的特点就是k可分 那么k - 1一定可分
        # 这个是找最大值
        def isdividable(num):
            t = 0
            for candy in candies:
                t += candy // num
                if t >= k:
                    return True
            return False

        low, high = 0, 10 ** 7
        while low < high:
            mid = (low + high + 1) // 2
            if isdividable(mid):
                low = mid
            else:
                high = mid - 1
        return low

def main():
    sol = Solution()
    _input = ([5, 8, 6], 3)
    _output = sol.maximumCandies(*_input)
    print(_output)

if __name__ == '__main__':
    main()
