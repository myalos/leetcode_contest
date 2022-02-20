from typing import *

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
