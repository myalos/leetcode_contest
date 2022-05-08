from typing import *

# 这题是用古老的手机打字
# 打出字母s要按7 4次，类似地 按5 两次可以得到字母k
# 已知按的数字序列 输出所有可能字母序列
# 答案对10^9 + 7取模 注意哦 1e9 + 7 是一个float类型的

class Solution:
    def countTexts(self, pressedKeys : str) -> int:
        MOD, OFFSET = int(1e9 + 7), 2
        digit_slice = [[] for _ in range(2, 10)]
        # digit_slice[0] 表示数字'2' 每个连续区段的长度
        prev, cnt = pressedKeys[0], 1
        # prev表示上一个字符，cnt表示一连串字符的个数
        max3, max4, ans = 0, 0, 1
        # max3 是3字符键位最长子数组的长度
        for i in range(1, len(pressedKeys)):
            ch = pressedKeys[i]
            if ch != prev: # 一组连续的字符结束了，到下一组了
                index = int(prev) - OFFSET
                digit_slice[index].append(cnt)
                if index in (5, 7):
                    max4 = max(max4, cnt)
                else:
                    max3 = max(max3, cnt)
                prev = ch
                cnt = 1
            else:
                cnt += 1
        # 下面是处理最后一组，其实在原始字符串中加一个特殊字符就可以使得下面的代码去掉
        index = int(prev) - OFFSET
        digit_slice[index].append(cnt)
        if index in (5, 7):
            max4 = max(max4, cnt)
        else:
            max3 = max(max3, cnt)
        dp3, dp4 = [1] * (max3 + 1), [1] * (max4 + 1)
        for i in range(1, max3 + 1):
            dp3[i] = dp3[i - 1] + (dp3[i - 2] if i > 1 else 0) + (dp3[i - 3] if i > 2 else 0)
            dp3[i] = dp3[i] % MOD

        for i in range(1, max4 + 1):
            dp4[i] = dp4[i - 1] + (dp4[i - 2] if i > 1 else 0) + (dp4[i - 3] if i > 2 else 0) + (dp4[i - 4] if i > 3 else 0)
            dp4[i] = dp4[i] % MOD
        for i in range(2, 10):
            index = i - OFFSET
            if index in (5, 7):
                for num in digit_slice[index]:
                    ans = (ans * dp4[num]) % MOD
            else:
                for num in digit_slice[index]:
                    ans = (ans * dp3[num]) % MOD
        return ans


def main():
    sol = Solution()
    _input = ("22233", )
    _input1 = ("222222222222222222222222222222222222", )
    _output = sol.countTexts(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
