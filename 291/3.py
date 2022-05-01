from typing import *

class Solution:
    def countDistinct(self, nums:List[int], k : int, p : int) -> int:
        # 暴力算法是先暴力得到不同的子数组
        # 然后对子数组进行筛选
        # 子数组的个数不是那么吓人
        # 从[1, 2, 3, 4]可以看出新加一个元素，会增加的数组个数是数组中元素个数（每个元素都可以作为开头）
        ans, n = set(), len(nums)
        remainder = [int(num % p == 0) for num in nums]
        # prefix sum
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + remainder[i - 1]

        for i in range(n):
            for j in range(i, n):
                if prefix_sum[j + 1] - prefix_sum[i] > k:
                    break
                ans.add(tuple(nums[i:j+1]))
        return len(ans)




def main():
    sol = Solution()
    _input = ([2,3,3,2,2],2,2)
    _output = sol.countDistinct(*_input)
    print(_output)

if __name__ == '__main__':
    main()
