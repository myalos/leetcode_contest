from typing  import *

# WA: [31,15,92,84,19,92,55] 虽然92在后面有，但是可以31，15然后15，15
# 如果nums里面有两个不同的元素那么栈一定不为空

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        # 如果nums里面的元素都是一样的
        if len(set(nums)) == 1:
            return -1
        # k次操作最多可以栈顶的元素可以是0 到 k，但是k - 1 的元素不可能最后的栈顶，因为一直弹k - 1次才解放出第k - 1个元素，然后还剩1次操作机会了，是不可能把第k - 1个元素保留下来的
        # 所以如果k - 1位置上的是最大值 就选第二大的数，不然就选最大数
        # 又有一个问题 返回的时候只能返回不在栈里面的
        # 下面的最大值 指的是下表0 ... k的值中的最大值
        # 如果整体个数小于k的话 那么就可以取到这个数组中的最大值
        if len(nums) < k:
            return max(nums)
        # 如果整体个数等于k
        if len(nums) == k:
            if k == 2:
                return nums[0]
            return max(max(nums[:-2]), nums[-1])
        # 如果最大值在下标为k的位置上，这个情况可以作为baseline
        ans = nums[k]
        # 如果最大值在下标为k - 1的位置上
        # 这个情况合并到提取0 ... k - 2的最大值中
        # 如果最大值在0 ... k - 2中且也在k - 1 ...中
        candidate = sorted(nums[:k-1], reverse=True)
        #  检查candidate里面的数字是否在k - 1之后出现过
        for i in range(len(candidate)):
            flag = True
            for j in range(k - 1, len(nums)):
                if candidate[i] == nums[j]:
                    flag = False
                    break
            if flag:
                return max(ans, candidate[i])

        # 如果最大值只在 0 ... k - 2中
        return ans

# 后来发现这题放回元素的时候 不需要考虑栈里面有没有这个元素
# 那这题就不难了

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]      
        if len(nums) == 1:
            return nums[0] if k % 2 == 0 else -1
        if len(nums) < k:
            return max(nums)
        if k == 1:
            return nums[1]
        if len(nums) == k:
            return max(nums[:-1])
        return max(max(nums[:k-1]), nums[k])

def main():
    sol = Solution()
    _input = ([5,2,2,4,0,6], 4)
    _output = sol.maximumTop(*_input)
    print(_output)

if __name__ == '__main__':
    main()
