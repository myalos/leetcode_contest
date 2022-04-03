from typing import *

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # 处理数据
        current_hour = int(current.split(':')[0])
        current_minute = int(current.split(':')[1])
        correct_hour = int(correct.split(':')[0])
        correct_minute = int(correct.split(':')[1])

        diff = (correct_hour - current_hour) * 60 + (correct_minute - current_minute)
        ans = 0
        for operation in (60, 15, 5, 1):
            ans += diff // operation
            diff = diff % operation
        return ans

def main():
    sol = Solution()
    _input = ("02:30", "04:35")
    _input1 = ("11:00", "11:01")
    _output = sol.convertTime(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
