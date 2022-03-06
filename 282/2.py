class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        _s = Counter(s)
        _t = Counter(t)
        # 两个Counter 求并
        union = _s | _t
        total, _s_count, _t_count = 0, 0, 0
        for item in union.items():
            total += item[1]
        for item in _s.items():
            _s_count += item[1]
        for item in _t.items():
            _t_count += item[1]
        return total * 2 - _s_count - _t_count    

def main():
    sol = Solution()
    _input = ("leetcode", "coats")
    _output = sol.minSteps(*_input)
    print(_output)

if __name__ == '__main__':
    main()
