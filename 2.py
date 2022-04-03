from typing import *

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # 用一个字典记录 参赛选手和输掉比赛次数的映射
        ans = [[], []]
        from collections import defaultdict
        mapping = defaultdict(int)
        for match in matches:
            mapping[match[1]] += 1
            mapping[match[0]]
        for candidate in sorted(mapping.keys()):
            if mapping[candidate] == 0:
                ans[0].append(candidate)
            if mapping[candidate] == 1:
                ans[1].append(candidate)
        return ans



def main():
    sol = Solution()
    _input = ([[2, 3], [1, 3], [5, 4], [6, 4]], )
    _output = sol.findWinners(*_input)
    print(_output)

if __name__ == '__main__':
    main()
