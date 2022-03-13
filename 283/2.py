from typing import *
import ipdb

# WA 错误原因一是如果nums没有被排序
# 加上了num.sort() TLE，原因是题目中k可以达到10^9 所以遍历k是不行的

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        index = 0
        candidate = 1
        num = len(nums)
        ans = 0
        while k > 0 and index < num:
            if candidate < nums[index]:
                ans += candidate
                k -= 1
                candidate += 1
            elif candidate  == nums[index]:
                index += 1
                candidate += 1
            else:
                index += 1

        while k > 0:
            ans += candidate
            candidate += 1
            k -= 1
        return ans


# 这个问题出在如果小于k的数中有两个是一样的话 我的1到k是没有加两个一样的数的
class Solution1:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        # 首先找到最理想的情况
        ans = (k + 1) * k // 2 # 选出1到k k个正整数
        index, candidate, num = 0, k + 1, len(nums)
        remain = 0 # 理想情况下，剩余需要填的数就是remain了
        nums.sort()
        # 首先找出在nums输出里面 小于k的所有数，因为nums是有序的，所以顺着找就行了
        # 找到一个就要把这个数从ans里面减去
        while index < num:
            if k >= nums[index]:
                ans -= nums[index]
                remain += 1
            else:
                break
            index += 1
        # candidate从k + 1开始
        ipdb.set_trace()
        while remain > 0 and index < num:
            if candidate < nums[index]:
                ans += candidate
                remain -= 1
                candidate += 1
            elif candidate == nums[index]:
                candidate += 1
                index += 1
            else:
                index += 1
        while remain > 0:
            ans += candidate
            candidate += 1
            remain -= 1
        return ans

# WA 错误原因是  ans += (prev + nums[i]) * item // 2这里
# 如果item项数是等于k 而下雨nums[i] - prev - 1的 那么末项就不是nums[i]了
# 改成 (prev + 1 + prev + item) 就OK了
class Solution3:
    # 这个算法的思想是求nums[i]相邻两项之间空隙的和
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans, prev = 0, 0
        nums.sort()
        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] <= prev + 1: # 考虑到相同元素的存在 19 19， 19 20都算没有空隙的
                prev = nums[i] 
                continue
            item = min(k, nums[i] - prev - 1) # 从prev + 1到nums[i] - 1总共有nums[i] - prev - 2 + 1个数
            ans += (prev + 1 + prev + item) * item // 2
            # 首项是prev + 1 末项是 nums[i] - 1
            k -= item
            prev = nums[i]
        if k > 0:
            ans += (nums[-1] + 1 + nums[-1] + k) * k // 2
        return ans

def main():
    sol = Solution1()
    _input = ([1, 4, 25, 10, 25], 2)
    _input1 = ([5, 6], 6)
    _input3 = ([96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84], 35)
    _output = sol.minimalKSum(*_input3)
    print(_output)

if __name__ == '__main__':
    main()

