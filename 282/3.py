from typing import *
# 我的想法是二分找到最小的时间
# 这个错了好多遍
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def count(moment):
            res = 0
            for _t in time:
                res += moment // _t
            return res
        
        # 即使把sum(time) 换成非常大的数 还是不行
        # 后来发现可能数字还是不够大，我改成了 min(time) * totalTrips 就搞定了
        # 我觉得这个题目需要看一下题解，因为我这个算法有点girigiri
        low, high = 1, min(time) * totalTrips
        while low < high:
            mid = (low + high) // 2
            if count(mid) < totalTrips:
                low = mid + 1
            else:
                high = mid
        return low

def main():
    sol = Solution()
    _input = ([1, 2, 3], 5)
    _output = sol.minimumTime(*_input)
    print(_output)

if __name__ == '__main__':
    main()

