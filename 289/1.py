from typing import *

class Solution:
    def digitSum(self, s : str, k : int) -> str:
        n = len(s)
        while n > k:
            temp = s
            s = ''
            for i in range(0, n, k):
                res = 0
                for j in range(k):
                    if (i + j) < n:
                        res += int(temp[i + j])
                s += str(res)
            n = len(s)
        return s

def main():
    sol = Solution()
    _input = ("11111222223", 3)
    _input1 = ("00000000", 3)
    _output = sol.digitSum(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
