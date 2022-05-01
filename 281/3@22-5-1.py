from typing import *

class Solution:
    def repeatLimitedString(self, s : str, repeatLimit : int) -> str:
    from collections import Counter
    characters = Counter(s)
    chs = list(sorted(characters.keys(), reverse=True))
    # high记录的是字典序最大的字符的索引，low记录的是high 下一个字典序的索引
    # 分为两个stage 一个是增加最大字符 repeatLimit次 另一个stage是增加下一个字符1次，如果只剩这个字符了就加repeatLimit次
    ans, low, n, stage, high = "", 0, len(chs), 0, 0
    while high < n:
        if stage == 0:
            ch = chs[high]
            _min = min(repeatLimit, characters[ch])
            ans += _min * ch
            characters[ch] -= _min
            if characters[ch] == 0:
                # 更新最大字典序字符的索引
                # 同时继续进行high的stage
                while high < n and characters[chs[high]] == 0:
                    high += 1
                stage = 0
            else:
                stage = 1
        else:
            if low <= high:
                low = high + 1
            while low < n and characters[chs[low]] == 0:
                low += 1
            if low >= n:
                # 接下来会到high，不管high是否有效，算法都应该停止
                break
            ch = chs[low]
            _min = 1
            if high == n: # 说明只剩下low字符了
                _min = min(repeatLimit, characters[ch])
            ans += _min * ch
            characters[ch] -= _min
            stage = 0

    return ans

# 时间 368ms 击败了77.25%的用户

# 找到一个写的简单的代码

class Solution:
    def repeatLimitedString(self, s : str, repeatLimit : int) -> str:
        dic = collections.Counter(s)
        l = [[x, dic[x]] for x in dic]
        l.sort()
        pres, res = l.pop(), ""
        # 这个代码里面的pres就是最高位
        while l:
            if pres[1] <= repeatLimit:
                res += pres[0] * pres[1]
                pres = l.pop()
            else:
                res += pres[0] * repeatLimit + l[-1][0]
                if l[-1][0] == 1:
                    l.pop()
                else:
                    l[-1][1] -= 1
                pres[1] -= repeatLimit
        return res + pres[0] * min(pres[1], repeatLimit)
