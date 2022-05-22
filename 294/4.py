# 0开始的整数数组strength，其中strength[i]表示第i位巫师的力量值。对于连续的一组巫师也就是strength的子数组，总力量定义为 巫师中最弱的能力值和组中所有巫师的个人力量之和的乘积
# 最后返回所有巫师组的总力量之和。对答案10**9+7取余后返回

# 参考的 灵茶山艾府的代码
from typing import *

class Solution:
    def totalStrength(self, strength : List[int]) -> int:
        from itertools import accumulate
        # 我一般是用int(1e9 + 7) 这个没有10 ** 9 + 7写的漂亮
        ans, MOD = 0, 10 ** 9 + 7
        # 首先用单调栈来获取i左边 第一个小于strength[i]的值和获取i右边第一个小于等于strength[i]的值
        left, right, stack = [-1] * len(strength), [len(strength)] * len(strength), []
        # 前缀和的前缀和的写法
        # ss = list(accumulate(accumulate(strength, initial=0), initial=0))
        ss = list(accumulate([0] + list(accumulate([0] + strength))))
        for i in range(len(strength)):
            while stack and strength[stack[-1]] >= strength[i]:
                right[stack.pop()] = i
            if stack : left[i] = stack[-1]
            stack.append(i)
        # 对于索引i需要计算的闭区间的就是[left[i] + 1, right[i] ]
        # r从left到right l从left到r sum[r] - sum[l]
        for i in range(len(strength)):
            l, r = left[i] + 1, right[i] - 1
            tot = (i - l + 1) *(ss[r + 2] - ss[i + 1]) - (r -i + 1) * (ss[i + 1] - ss[l])
            ans += strength[i] * tot
        return ans % MOD


def main():
    sol = Solution()
    _input = ([1, 3, 1, 2], )
    _output = sol.totalStrength(*_input)
    print(_output)

if __name__ == '__main__':
    main()
