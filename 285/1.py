from typing  import *

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        temp = nums
        nums = [temp[0]]
        prev = temp[0]

        # 将连续相同的值 合并成一个值
        for i in range(1, len(temp)):
            if temp[i] != prev:
                nums.append(temp[i])
            prev = temp[i]

        # 只有两个值的时候构不成 波峰也构不成波谷
        if len(nums) <= 1:
            return 0
        for i in range(1, len(nums) - 1):
            if nums[i] < nums[i + 1] and nums[i] < nums[i - 1]:
                ans += 1
            if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                ans += 1
        return ans


def main():
    sol = Solution()
    _input = ([2, 4, 1, 1, 6, 5],)
    _output = sol.countHillValley(*_input)
    print(_output)

if __name__ == '__main__':
    main()
