from typing import *

# 标签：最值

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full:int, partial: int) -> int:
        # 完善的花园是用完善的花园数目，不完善的花园用的是花的最小数目
        # 增加分数的方式有两种 一种是增加完善花园数目，另一种是增加不完善花园的花的最小数目
        # 这个题有点像背包，newFlowers是背包体积，完善花园就是物品，加了一个不完善花园的内容
        # 这题增加不完善花园的花的最小数目比较像上一题k次增加后的最大乘积

        # 下面的代码是copy的灵茶山艾府的

        flowers.sort()
        n = len(flowers)
        if flowers[0] >= target:
            return n * full
        leftFlowers = newFlowers - target * n
        for i in range(n):
            flowers[i] = min(flowers[i], target)
            leftFlowers += flowers[i]
        ans, x, sumFlowers = 0, 0, 0
        for i in range(n + 1):
            if leftFlowers >= 0:
                while x < i and flowers[x] * x - sumFlowers <= leftFlowers:
                    sumFlowers += flowers[x]
                    x += 1
                beauty = (n - i) * full
                if x:
                    beauty += min((leftFlowers + sumFlowers) // x, target - 1) * partial
                ans = max(ans, beauty)
            if i < n:
                leftFlowers += target - flowers[i]
        return ans









def main():
    sol = Solution()
    _input = ([2,4,5,3],10, 5, 2, 6)
    _output = sol.maximumBeauty(*_input)
    print(_output)

if __name__ == '__main__':
    main()
