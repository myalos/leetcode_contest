from typing import *

class Solution:
    def appealSum(self, s : str) -> int:
        # 这题和上题很像
        # 这题的特点是不需要考虑重复的问题
        from collections import defaultdict
        ans, n = 0, len(s)
        index = defaultdict(int)
        # index[c] = 0表示目前字符c还没有出现过
        # 新加入一个c之后，考察每个字符所在的位置，每个字符出现的位置就是这个字符能提供的战斗力
        for i in range(n):
            ch = s[i]
            index[ch] = 0
            ans += i + 1 + sum(index.values())
            index[ch] = i + 1
        return ans

def main():
    sol = Solution()
    _input = ("code", )
    _input1 = ("abbca", )
    _output = sol.appealSum(*_input)
    print(_output)

if __name__ == '__main__':
    main()
