# 这个代码是个错的 72个测试样例 卡在第69个了
# 这是有问题的代码
# add是添加[left, right]
# count就是返回之前所有add 形成区间的交集所含数字的个数
from typing import *

class CountIntervals:
    def __init__(self):
        # 区间划分 左闭右开
        self.intervals = []
        self.cnt = 0

    def add(self, left : int, right : int) -> None:
        import bisect
        save,n = left, len(self.intervals)
        # 我想让add量级在O(logn) 但事实上很有可能达不到，而是变成了O(n)
        left_index = bisect.bisect_left(self.intervals, left)
        right_index = bisect.bisect_left(self.intervals, right + 1)
        # 先计算增加了多少内容
        cursor = left_index
        while cursor < right_index:
            if cursor % 2 == 0:
                self.cnt += self.intervals[cursor] - left
            left = self.intervals[cursor]
            cursor += 1
        if right_index % 2 == 0:
            self.cnt += right + 1 - left

        # 再改变数据结构
        # 有些区域是需要合并的
        # 下面这个合并方法有问题
        # 问题出在
        # [10, 28, 46, 51] 上面add(15, 35)
        # 我的算法会得到的intervals是[10, 15, 36, 46, 51]
        # 而实际上这个15应该是不要的
        if left_index == right_index and left_index % 2 == 1:
            return
        temp = self.intervals[:left_index]
        if left_index == n or self.intervals[left_index] != save:
            temp.append(save)
        if right_index == n or self.intervals[right_index] != right + 1:
            temp.append(right + 1)
        self.intervals = temp + self.intervals[right_index:]

    def count(self) -> int:
        return self.cnt

# 要改一下
class CountIntervals1:
    def __init__(self):
        # 区间划分 左闭右开
        self.intervals = []
        self.cnt = 0

    def add(self, left : int, right : int) -> None:
        import bisect
        save,n = left, len(self.intervals)
        # 我想让add量级在O(logn) 但事实上很有可能达不到，而是变成了O(n)
        left_index = bisect.bisect_left(self.intervals, left)
        right_index = bisect.bisect_left(self.intervals, right + 1)
        # 先计算增加了多少内容
        cursor = left_index
        while cursor < right_index:
            if cursor % 2 == 0:
                self.cnt += self.intervals[cursor] - left
            left = self.intervals[cursor]
            cursor += 1
        if right_index % 2 == 0:
            self.cnt += right + 1 - left

        # 再改变数据结构
        # 有些区域是需要合并的
        # 下面这个合并方法有问题
        # 问题出在
        # [10, 28, 46, 51] 上面add(15, 35)
        # 我的算法会得到的intervals是[10, 15, 36, 46, 51]
        # 而实际上这个15应该是不要的
        #if save == 15:
        #    print('what')
        #    __import__('ipdb').set_trace()
        if left_index == right_index and left_index % 2 == 1:
            return
        temp = self.intervals[:left_index]
        if left_index == n or left_index % 2 == 0:
            temp.append(save)
        if right_index == n or self.intervals[right_index] != right + 1 and right_index % 2 == 0:
            temp.append(right + 1)
        self.intervals = temp + self.intervals[right_index:]

    def count(self) -> int:
        return self.cnt


def main():
    cc = CountIntervals1()
    #cc.add(2, 3)
    #print(cc.count())
    #cc.add(7, 10)
    #print(cc.count())
    #cc.add(5, 8)
    #print(cc.count())

    cc1 = CountIntervals1()
    #cc1.add(8, 43)
    #print(cc1.intervals)
    #cc1.add(13, 16)
    #print(cc1.intervals)
    #cc1.add(26, 33)
    #print(cc1.intervals)
    #cc1.add(28, 36)
    #print(cc1.intervals)
    #cc1.add(29, 37)
    #print(cc1.count())

    cc2 = CountIntervals1()
    #cc2.add(10, 27)
    #print(cc2.intervals)
    #cc2.add(46, 50)
    #print(cc2.intervals)
    #cc2.add(15, 35)
    #print(cc2.intervals)
    #cc2.add(12, 32)
    #print(cc2.intervals)
    #cc2.add(7, 15)
    #print(cc2.intervals)
    #cc2.add(49, 49)
    #print(cc2.intervals)
    #print(cc2.count())

    cc3 = CountIntervals1()
    #cc3.add(1, 1)
    #print(cc3.intervals)
    #cc3.add(2, 2)
    #print(cc3.intervals)
    #cc3.add(3, 3)
    #print(cc3.intervals)
    #cc3.add(1, 1)
    #print(cc3.intervals)
    #cc3.add(1, 1)
    #print(cc3.intervals)
    #print(cc3.count())

    cc4 = CountIntervals1()



if __name__ == '__main__':
    main()
