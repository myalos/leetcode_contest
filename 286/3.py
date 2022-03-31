from typing import *

# WA: 错误原因是可能这个回文数不存在 也就是说base + query - 1进位了
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) ->List[int]:
        # 回文数可以拆分左边的 中间的 右边的，中间的可能是没有的
        # 根据左边和中间的就可以还原出整个的 这个就有点像信息压缩
        leftlen = (intLength + 1) // 2
        ans = []
        base = 10 ** (leftlen - 1)
        for query in queries:
            left = base + query - 1
            left = str(left)
            # 补上下面的就解决了WA了
            if len(left) != len(str(base)):
                ans.append(-1)
                continue
            left = left + (left[-2::-1] if intLength % 2 else left[::-1]) # 这里的括号要注意
            ans.append(int(left))
        return ans

def main():
    sol = Solution()
    _input = ([1, 2, 3, 4, 5, 90], 3)
    _input1 = ([2, 4, 6], 4)
    _output = sol.kthPalindrome(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
