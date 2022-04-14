from typing import *
import functools

def debug(function):
    @functools.wraps(function)
    def _debug(*args, **kargs):
        print(args)
        result =  function(*args, **kargs)
        print(result)
        input("next")
        return result
    return _debug

# 感觉这个题挺有意思的
# WA: 基本的背包题目我都写不对
# 第一个测试数据我的输出是
#[0, 0, 0, 0, 1, 1, 3, 2, 1, 2, 3, 1]
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        dp, ans = {}, {}
        def dfs(arrows : int, position : int):
            if (arrows, position) in dp:
                return dp[(arrows, position)], ans[(arrows, position)]
            if position == 0 or arrows == 0:
                dp[(arrows, position)] = 0
                ans[(arrows, position)] = dict()
                return 0, {}
            lans, rans, lpos, rpos = 0, 0, {}, {}
            if arrows == 5 and position == 9:
                __import__('ipdb').set_trace()
            if arrows > aliceArrows[position]:
                lans, lpos = dfs(arrows - aliceArrows[position] - 1, position - 1)
                lans += position
                lpos[position] = aliceArrows[position] + 1
            # 执行到这一步的时候 lpos里面是{4: 1, 5: 1, 8: 1, 9: 2}
            rans, rpos = dfs(arrows, position - 1)
            # 执行完这一步的时候 lpos 里面发生了变化 但这不是我的意图
            if lans > rans:
                dp[(arrows, position)] = lans
                ans[(arrows, position)] = lpos
                return lans, lpos
            if lans == rans:
                dp[(arrows, position)] = lans
                if sum(lpos.values()) < sum(rpos.values()):
                    ans[(arrows, position)] = lpos
                else:
                    ans[(arrows, position)] = rpos
                return dp[(arrows, position)], ans[(arrows, position)]
            dp[(arrows, position)] = rans
            ans[(arrows, position)] = rpos
            return rans, rpos

        _, finalpos = dfs(numArrows, 11)
        ans = [0] * 12
        for key, value in finalpos.items():
            ans[key] = value
            numArrows -= value
        if numArrows > 0:
            ans[0] = numArrows
        return ans


class Solution1:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        dp, ans = {}, {}
        def dfs(arrows : int, position : int): # arrows表示还剩arrows之箭，position表示现在考虑的是position位置
            if (arrows, position) in dp:
                # 索引(arrows, position)可以去掉外面的括号变成arrows, position
                return dp[(arrows, position)], ans[(arrows, position)]
            if position == 0 or arrows == 0:
                dp[(arrows, position)] = 0
                ans[(arrows, position)] = dict()
                return 0, {}
            lans, rans, lpos, rpos = 0, 0, {}, {}
            if arrows > aliceArrows[position]: # 如果剩下的箭 可以拿下这个position位置的分数的话
                lans, _lpos = dfs(arrows - aliceArrows[position] - 1, position - 1)
                # 这里是关键
                lpos = _lpos.copy()
                lans += position
                lpos[position] = aliceArrows[position] + 1
            rans, _rpos = dfs(arrows, position - 1)
            rpos = _rpos.copy()
            if lans > rans:
                dp[(arrows, position)] = lans
                ans[(arrows, position)] = lpos
                return lans, lpos
            dp[(arrows, position)] = rans
            ans[(arrows, position)] = rpos
            return rans, rpos

        _, finalpos = dfs(numArrows, 11)
        ans = [0] * 12
        for key, value in finalpos.items():
            ans[key] = value
            numArrows -= value
        if numArrows > 0:
            ans[0] += numArrows
        return ans

def main():
    sol = Solution1()
    _input = (9, [1,1,0,1,0,0,2,1,0,1,2,0])
    _output = sol.maximumBobPoints(*_input)
    print(_output)

if __name__ == '__main__':
    main()
