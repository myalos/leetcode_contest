from typing import *

class Solution:
    def fullBloomFlowers(self, flowers : List[List[int]], persons : List[int]) -> List[int]:
        # 这个题目题意简单易懂 我感觉这题的解法就和我上题解错的方法是一样的
        # 将start time单独拿出来排序，将end time也单独拿出来排序
        # 对于每个人来的时间t，找出最大的小于等于t的start time和最小的大于等于t的end time 然后求最小值
        # 这个想法有问题 反例子 [1, 2] [9, 10] 然后person在5
        # 参考大佬的思路 就是将开了的花减去凋谢的花
        import bisect
        start = sorted([flowers[i][0] for i in range(len(flowers))])
        end = sorted([flowers[i][1] for i in range(len(flowers))])
        ans = []
        for person in persons:
            ans.append(bisect.bisect_right(start, person) - bisect.bisect_left(end, person))
        return ans





def main():
    sol = Solution()
    _input = ([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11])
    _input1 = ([[1, 10], [3, 3]], [3, 3, 2])
    _output = sol.fullBloomFlowers(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
