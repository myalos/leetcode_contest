from typing import *

# 感觉这个题目挺有意思的

# 这个解法的问题就是如果我一个开始选了一个轮胎，那么对于其余的轮胎来讲，flag为0的项应该从堆中去掉，flag为1的项在堆中保留
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        import heapq
        from functools import partial
        
        heap = []
        ans = 0
        
        for item in tires:
            _item = [item[0], item[1], 0]
            heap.append(_item)
            # 下面表示如果换成这个轮胎 需要的时间
            _new_item = [item[0] + changeTime, item[1], 1]
            heap.append(_new_item)
        
        push = partial(heapq.heappush, heap)
        pop = partial(heapq.heappop, heap)
        
        for _ in range(numLaps):
            f, r, flag = pop()
            ans += f
            if flag == 1: # 有用到changetime
                push([(f - changeTime) * r, r, 0])
                push([f, r, 1])
            else:
                push([f*r, r, 0])
        return ans

# 换了个dp的思路，结果发现会超时

class Solution1:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        num_tires = len(tires)
        dp = [[1000000000] * len(tires) for _ in range(numLaps + 1)]
        assist = [[0] * len(tires) for _ in range(numLaps + 1)]
        # dp[i][j] 表示跑i圈 最后用的是第j个轮胎 最小的耗时
        for i in range(num_tires):
            dp[1][i] = tires[i][0]
            assist[1][i] = 0 # 达到这个dp状态之前用过多少次i号胎
        
        for i in range(1, numLaps + 1):
            for j in range(num_tires):
                # 要么是同一个轮胎跑的 要么就不是
                # 感觉还要套一个循环 时间爆了
