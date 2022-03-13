from typing  import *

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = []
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                indices.append(i)

        ans = set()
        for index in indices:
            ans.add(index)
            for offset in range(1, k + 1):
                ans.add(max(0, index - offset))
                ans.add(min(offset + index, n - 1))
        return list(ans)


def main():
    sol = Solution()
    _input = ([3,4,9,1,3,9,5], 9, 1)
    _input1 = ([2,2,2,2,2], 2, 2)
    _output = sol.findKDistantIndices(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
