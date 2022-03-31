from typing import *

#感觉第i个和第i + 1个不同是一个局部信息，而找至少需要删除的元素是一个全局信息
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n, ind, ans = len(nums), 0, 0
        while ind < n - 1:
            if nums[ind] == nums[ind + 1]: #逐对相消 后第i个元素在最左边
                ans += 1
            else:
                ind += 1 # 逐对相消后，发现最左边两个元素不等，就把这两个元素相消
            ind += 1

        if (n - ans) % 2: # n个元素删掉ans个元素后还剩的元素为奇数个 就把最后一个元素删掉
            ans += 1
        return ans


def main():
    sol = Solution()
    _input = ([1, 1, 2, 3, 5], )
    _output = sol.minDeletion(_input)
    print(_output)

if __name__ == '__main__':
    main()
