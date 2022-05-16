# words列表 words[i] 由小写英文字符组成
# 在一步操作中，需要选出任一下标i，从words中删除words[i]。其中下标i需要同时满足两个条件
# 0 < i < words.length
# words[i - 1]和words[i]是字母异位词
# 只要可以选出满足条件的下标就一直执行这个操作
# 在执行所有操作后，返回words
# 字母异位词是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好出现一次

from typing import *

class Solution:
    def removeAnagrams(self, words:List[str]) -> List[str]:
        from collections import Counter
        def check(a, b):
            return Counter(a) == Counter(b)
        ans = []
        for word in words:
            if ans and check(ans[-1], word):
                continue
            ans.append(word)
        return ans

def main():
    sol = Solution()
    _input = (["abba", "baba", "bbaa", "cd", "cd"], )
    _output = sol.removeAnagrams(*_input)
    print(_output)

if __name__ == '__main__':
    main()
