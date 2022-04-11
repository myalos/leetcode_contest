from typing import *

class Solution:
    def maximumProduct(self, nums: List[int], k : int) -> int:
        mod = 10 ** 9 + 7
        # 如果是给原数组加1 那么应该是加最小的数，给最小数加1 相当于给总乘积加的数最大
        # 原数组的总乘积可以看成a * b 如果a是最小值 那么新的总乘积就是(a + 1) * b
        # 相当于多加了一个b
        # 如果给原数组加2，如果是给同一个数加2 那么肯定是给最小值加2，如果是给不同数加1
        # 那么应该是给最小的两个值加1,由此可知这题要用贪心（说的有点不严谨，但是意思应该比较清楚了）
        nums.sort()
        n = len(nums)
        if n == 1: return nums[0] + k
        # diff[i] = nums[i + 1] - nums[i]
        diff = [nums[i + 1] - nums[i] for i in range(n - 1)]
        # 定位k的位置
        position = 0
        while position < n - 1:
            # diff[position] 是 nums[position + 1] 到 nums[position]的差，乘以position + 1是因为
            # 前面nums[0 ... position]都被填平成了nums[position] 那么就要有position + 1个数要填成nums[position + 1]
            if k < diff[position] * (position + 1):
                break
            k -= diff[position] * (position + 1)
            position += 1
        ans = 1
        # position 后面的数字
        for i in range(position + 1, n):
            ans = (ans * nums[i]) % mod
        # 0 .. position - 1已经填成position了 0 .. position 每个加k // (position + 1) 剩余的 k % (position + 1)
        # 也分摊出去
        a = k // (position + 1)
        b = k % (position + 1)
        base = nums[position]
        # b个数字是要加上a + 1，其余数字是加上a
        for _ in range(b):
            ans = (ans * (a + base + 1)) % mod
        for _ in range(position + 1 - b):
            ans = (ans * (a + base)) % mod
        return ans

# 下面是大佬的解法，用堆来模拟每次操作
class Solution1:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heapreplace
        MOD = 10 ** 9 + 7
        heapify(nums)
        while k:
            # 这里的heapreplace方法 相当于heappop()加上heappush()方法
            heapreplace(nums, nums[0] + 1)
            k -= 1
        ans = 1
        for num in nums:
            ans = ans * num % MOD
        return ans


def main():
    sol = Solution()
    _input = ([6, 3, 3, 2], 2)
    _output = sol.maximumProduct(*_input)
    print(_output)

if __name__ == '__main__':
    main()
