from typing import *

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if word.startswith(pref):
                ans += 1
        return ans

def main():
    sol = Solution()
    _input = (["pay","attention","practice","attend"], "at")
    _output = sol.prefixCount(*_input)
    print(_output)

if __name__ == '__main__':
    main()
