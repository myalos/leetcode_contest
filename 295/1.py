from typing import *

class Solution:
    def rearrangeCharacters(self, s : str, target : str) -> int:
        from collections import Counter
        dividend = Counter(s)
        divisor = Counter(target)
        ans = 10 ** 9
        for key in divisor:
            print(ans, dividend[key] , divisor[key])
            ans = min(ans, dividend[key] // divisor[key])
        return ans

def main():
    sol = Solution()
    _input = ("ilovecodingonleetcode", "code")
    _output = sol.rearrangeCharacters(*_input)
    print(_output)

if __name__ == '__main__':
    main()
