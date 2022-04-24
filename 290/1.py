from typing import *

class Solution:
    def intersection(self, nums : List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for array in nums:
            ans = ans & set(array)
        return list(sorted(ans))


class Solution1:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # 这里用set也行的
        from collections import Counter
        ans = None
        for array in nums:
            if not ans:
                ans = Counter(array)
            else:
                ans = ans & Counter(array)
        return list(sorted(ans.keys()))


def main():
    sol = Solution()
    _input = ([[3,1,2,4,5], [1,2,3,4], [3,4,5,6]], )
    _output = sol.intersection(*_input)
    print(_output)

if __name__ == '__main__':
    main()
