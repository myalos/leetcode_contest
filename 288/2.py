from typing import *

class Solution:
    def minimizeResult(self, expression: str) -> str:
        # 下面给的expression的长度范围是[3, 10] 感觉这题用暴力方法是没有问题的
        candidate_int, candidate_str = None, None
        left_operand, right_operand = expression.split('+')
        left_len, right_len = len(left_operand), len(right_operand)
        # 迭代切的位置，左边能切left_len个位置，第i个切口在索引为i的数字的左边
        # 右边能切right_len个位置，第i个切口在索引为i的数字的右边
        for i in range(left_len):
            for j in range(right_len):
                # a, b, c分别为括号左边的数 括号里面的数 括号右边的数
                a = 1 if i == 0 else int(left_operand[:i])
                c = 1 if j == right_len - 1 else int(right_operand[j + 1:])
                b = int(left_operand[i:]) + int(right_operand[:j + 1])
                if not candidate_int or (a * b * c < candidate_int):
                    candidate_int = a * b * c
                    candidate_str = left_operand[:i] + '(' + left_operand[i:] + '+' + right_operand[:j+1] + ')' + right_operand[j+1:]
        return candidate_str


def main():
    sol = Solution()
    _input = ("12+34", )
    _input1 = ("247+38", )
    _output = sol.minimizeResult(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
