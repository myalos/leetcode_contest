# 字符串s和字符letter 返回s中letter字符所占百分比
from typing import *

class Solution:
    def percentageLetter(self, s : str, letter : str) -> int:
        from collections import Counter
        c = Counter(s)
        return c[letter] * 100 // len(s)

def main():
    sol = Solution()
    _input = ("foobar", "o")
    _output = sol.percentageLetter(*_input)
    print(_output)

if __name__ == '__main__':
    main()
