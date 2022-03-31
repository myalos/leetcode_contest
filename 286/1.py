from typing import *


class Solution(object):
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        _set1, _set2 = set(), set()
        for item1 in nums1:
            if item1 not in nums2:
                _set1.add(item1)
        for item2 in nums2:
            if item2 not in nums1:
                _set2.add(item2)
        ans.append(list(_set1))
        ans.append(list(_set2))
        return ans

def main():
    sol = Solution()
    _input = ([1, 2, 3], [2, 4, 6])
    _output = sol.findDifference(*_input)
    print(_output)

if __name__ == '__main__':
    main()
