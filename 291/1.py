from typing import *

class Solution:
    def removeDigit(self, number : str, digit : str) -> str:
        # 我感觉有更漂亮的解法
        candidate = []
        for i in range(len(number)):
            if number[i] == digit:
                candidate.append(number[:i] + number[i+1:])
        return max(candidate)


def main():
    sol = Solution()
    _input = ("123", "3")
    _output = sol.removeDigit(*_input)
    print(_output)

if __name__ == '__main__':
    main()
