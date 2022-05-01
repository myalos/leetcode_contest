from typing import *

class Solution:
    def minimumCardPickup(self, cards:List[int]) -> int:
        from collections import defaultdict
        ans = len(cards) + 1
        position = defaultdict(int)
        for index in range(len(cards)):
            card = cards[index]
            if card in position:
                ans = min(ans, index - position[card] + 1)
            position[card] = index
        return ans if ans < len(cards) + 1 else -1



def main():
    sol = Solution()
    _input = ([3, 4, 2, 3, 4, 7], )
    _input1 = ([1, 0, 5, 3], )
    _output = sol.minimumCardPickup(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
