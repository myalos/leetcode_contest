from typing import *

class Solution:
    def largestInteger(self, num: int) -> int:
        # 马上想到的就是将所有奇数进行排序，所有偶数进行排序
        # 拆分数字
        weight, ans = 1, 0
        odd_digits, even_digits = [], []
        odd_weights, even_weights = [], []
        while num: # 处理顺序是从右往左
            # 当前数字是digit 然后其权重为weight
            digit = num % 10
            if digit % 2 == 0:
                even_digits.append(digit)
                even_weights.append(weight)
            else:
                odd_digits.append(digit)
                odd_weights.append(weight)
            weight *= 10
            num //= 10
        for digit, weight in zip(sorted(odd_digits), sorted(odd_weights)):
            ans += digit * weight
        for digit, weight in zip(sorted(even_digits), sorted(even_weights)):
            ans += digit * weight
        return ans


def main():
    sol = Solution()
    _input = (65875, )
    _output = sol.largestInteger(*_input)
    print(_output)

if __name__ == '__main__':
    main()
