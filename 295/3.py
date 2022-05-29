# 给你一个下标从0开始的整数数组nums
# 在一步操作中，移除所有满足nums[i - 1] > nums[i]的nums[i]，其中0 < i < nums.length
# 重复执行步骤，直到nums变为非递减数组，返回所需执行的操作数
from typing import *

# WA 这个题目 题意理解错误，每次删除的是nums[i - 1] > nums[i]的所有nums[i] 而不是第一个满足nums[i - 1] > nums[i] 的数组里面所有的nums[i]
class Solution:
    def totalSteps(self, nums : List[int]) -> int:
        # 数组里面第一个元素肯定是在最后的数组当中的
        removed = set()
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i] in removed:
                continue
            if nums[i + 1] < nums[i] and nums[i + 1] not in removed:
                ans += 1
                removed.add(nums[i + 1])
        return ans

# WA 21 / 86
# [10, 1, 2, 3, 4, 5, 6, 1, 2, 3]
# expected 6 got 0
# 通过这个示例 意识到题目没有那么简单
class Solution1:
    def totalSteps(self, nums : List[int]) -> int:
        ans, prev, index = 0, 0, 1
        while index < len(nums):
            if nums[index] >= nums[prev]:
                ans = max(ans, index - prev - 1)
                prev = index
            index += 1
        return ans

# 参考灵茶山艾府的解析
class Solution2:
    def totalSteps(self, nums : List[int]) -> int:
        st = []
        ans = 0
        for num in nums:
            # 将数字弹出 来维护单调栈的结构
            max_t = 0
            while st and st[-1][0] <= num:
                max_t = max(max_t, st.pop()[1])
            if st: max_t += 1
            else: max_t = 0
            ans = max(ans, max_t)
            st.append((num, max_t))
            print(num, max_t)
        return ans

def main():
    sol = Solution2()
    _input = ([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11], )
    _output = sol.totalSteps(*_input)
    print(_output)

if __name__ == '__main__':
    main()
