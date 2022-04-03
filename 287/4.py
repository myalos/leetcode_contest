from typing import *

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        from collections import Counter
        self.mapping = dict(zip(keys, values))
        # 这个dictionary是解密后所有允许的原字符串，统计有效字符串加密后
        # 的字符串
        self.count = Counter([self.encrypt(valid) for valid in dictionary])

    def encrypt(self, word1 : str) -> str:
        res = ''
        for ch in word1:
            if ch not in self.mapping.keys():
                return ''
            res += self.mapping[ch]
        return res

    def decrypt(self, word2 : str) -> int:
        return self.count[word2]

def main():
    sol = Encrypter(*[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd",
        "adbc", "badc", "dacb", "cadb", "cbda", "abad"]])
    print(sol.encrypt("abcd"))
    print(sol.decrypt("eizfeiam"))

if __name__ == '__main__':
    main()
