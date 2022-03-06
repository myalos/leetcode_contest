from typing import *


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        row_start = int(s[1])
        row_end = int(s[4])
        col_start = ord(s[0])
        col_end = ord(s[3])
        while col_start <= col_end :
            row_cursor = row_start
            while row_cursor <= row_end:
                ans.append(chr(col_start) + str(row_cursor))
                row_cursor += 1
            col_start += 1
        return ans


def main():
    sol = Solution()
    _input = ("K1:L2", )
    _output = sol.cellsInRange(*_input)
    print(_output)

if __name__ == '__main__':
    main()
