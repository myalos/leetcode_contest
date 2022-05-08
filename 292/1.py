from typing import *

# 字符串num，表示一个大整数，如果一个整数满足下述所有条件，则认为该整数是一个优质整数：
# 该整数是num的一个长度为3的子字符串
# 该整数由唯一一个数字重复3次组成
# 以字符串返回最大优质整数 如果不存在返回空字符串

class Solution:
    def largestGoodInteger(self, num : str)-> str:
        ans, max_digit = '', -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2] and int(num[i]) > max_digit:
                ans = num[i:i + 3]
                max_digit = int(num[i])
        return ans


def main():
    sol = Solution()
    _input = ("6777133339", )
    _output = sol.largestGoodInteger(*_input)
    print(_output)

if __name__ == '__main__':
    main()
