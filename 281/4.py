from typing import *

# 这个是copy的别人的解答
# https://leetcode-cn.com/problems/count-array-pairs-divisible-by-k/solution/tong-ji-yin-zi-chu-xian-ci-shu-by-endles-t5k8/
MX = 100001
divisors = [[] for _ in range(MX)]

for i in range(1, MX):
    for j in range(i, MX, i):
        divisors[j].append(i)

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        ans = 0
        cnt = defaultdict(int)
        # 相当于这个考虑的是v和v之前的所有元素
        for v in nums:
            ans += cnt[k / gcd(v, k)]
            for d in divisors[v]: # 这个是把v的所有因子的个数加1
                cnt[d] += 1
        return ans

def main():
    sol = Solution()
    _input = ([1, 2, 3, 4, 5], 2)
    _output = sol.coutPairs(*_input)
    print(_output)

if __name__ == '__main__':
    main()
