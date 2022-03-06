from typing  import *


# 感觉这题有点消消乐的味道
# !!! 消消乐就是栈啊！！！
# WA [899, 23, 23, 20677] 如果按照下面的算法的话，最后的结果是[899, 20677], 中间的23把20677给挡住了，20677是可以和899相消的
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if ans[-1] == 1 or nums[i] == 1 or gcd(ans[-1], nums[i]) == 1:
                ans.append(nums[i])
            else:
                t = ans.pop()
                ans.append(t // gcd(t, nums[i]) * nums[i])
        return ans

class Solution1:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        ans = [nums[0]]
        for i in range(1, len(nums)):
            while True:
                if len(ans) == 0 or ans[-1] == 1 or nums[i] == 1 or gcd(ans[-1], nums[i]) == 1:
                    ans.append(nums[i])
                    break
                # 如果nums[i]能和栈顶相消，那么更新nums[i]为消完后的内容，然后再看能不能继续消
                t = ans.pop()
                nums[i] = t // gcd(t, nums[i]) * nums[i]
        return ans

def main():
    sol = Solution1()
    _input = ([6,4,3,2,7,6,2], )
    _output = sol.replaceNonCoprimes(*_input)
    print(_output)

if __name__ == '__main__':
    main()
