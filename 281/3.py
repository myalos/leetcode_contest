from typing import *

# 题目
# 一个字符串s 和一个整数repeatLimit, 用s中的字符构造一个新字符串repeatLimitedString, 使任何字母连续出现的次数都不超过repeatLimit次。不必使用s中全部字符
# 返回字典序最大的 repeatLimitedString
#
# 输入 ("ccazazz", 3)
# 输出 "zzcccac"
# 输入2 ("aababab", 2)
# 输出2 "bbabaa"

# attemp1 WA 错误原因是 z有3个a有2个 每次最多一样的是2个，那么zzaza 肯定比zzaaz 要好
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # 这个算法的思路是把keys进行排序，然后每次填最多的keys
        ans = ''
        from collections import Counter
        c = Counter(s)
        flag = True
        # 获得Counter里面的键
        keys = list(c.keys())
        keys.sort(reverse=True)
        while flag:
            # 对于字符串，这个_ans不会和ans同步，修改ans不会改变_ans
            _ans = ans
            for x in keys:
                ans  += x * min(repeatLimit, c[x])
                c[x] -= min(repeatLimit, c[x])
            if len(_ans) == len(ans):
                flag = False
        return ans

class Solution1:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = ''
        from collections import Counter
        c = Counter(s)
        # 获得Counter里面的键
        keys = list(c.keys())
        keys.sort(reverse=True)
        num = len(keys) # num是全部key的数量
        key_index = 0 # key_index指向的是正在处理的key值

        # 感觉这个写法比较直观一点，不过时间上可能不是很好
        while True:
            # 找到第一个非空的key
            while key_index < num and c[keys[key_index]] == 0:
                key_index += 1
            if key_index == num:
                break
            ans  += keys[key_index] * min(repeatLimit, c[keys[key_index]])
            c[keys[key_index]] -= min(repeatLimit, c[keys[key_index]])
            if c[keys[key_index]] > 0:
                # 找到第一个非空的key
                key_index_temp = key_index + 1
                while key_index_temp < num and c[keys[key_index_temp]] == 0:
                    key_index_temp += 1
                if key_index_temp == num:
                    break
                # 然后将这个key对应的字符加到ans里面
                ans += keys[key_index_temp]
                c[keys[key_index_temp]] -= 1

        return ans

def main():
    sol = Solution1()
    _input = 'aababab'
    _output = sol.repeatLimitedString(_input, 2)
    print(_output)

if __name__ == '__main__':
    main()
