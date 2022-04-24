from typing import *

class Solution:
    def minimumRounds(self, tasks : List[int]) -> int:
        # 只有一种情况是完成不了的，那就是某个难度级别的任务只有1个
        from collections import Counter
        c = Counter(tasks)
        ans = 0
        for value in c.values():
            if value == 1:
                return - 1
            if value % 3 == 0:
                ans += value // 3
            elif value % 3 == 1:
                ans += (value - 4) // 3 + 2
            else:
                ans += (value - 2) // 3 + 1
        return ans

def main():
    sol = Solution()
    _input = ([2, 3, 3], )
    _input1 = ([2,2,3,3,2,4,4,4,4,4], )
    _output = sol.minimumRounds(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
