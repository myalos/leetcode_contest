from typing import *

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # 看这个数据 如果一个点在一个矩形内 只要同时满足x <= l and y <= h
        # 这个方法有问题，问题出在如果矩形都是细长的，都是l=1 h=10 和 l = 10 h = 1的，那么x, y 在5, 5理论上应该不在任何矩形中。
        ans = []
        rx = [rectangles[i][0] for i in range(len(rectangles))]
        ry = [rectangles[i][1] for i in range(len(rectangles))]
        rx.sort(reverse=True)
        ry.sort(reverse=True)
        for x, y in points:
            temp, low, high = None, 0, len(rx) - 1
            while low < high:
                mid = (low + high + 1) // 2
                if rx[mid] < x:
                    high = mid - 1
                else:
                    low = mid
            temp = low
            if rx[low] >= x:
                temp += 1
            low, high = 0, len(ry) - 1
            while low < high:
                mid = (low + high + 1) // 2
                if ry[mid] < y:
                    high = mid - 1
                else:
                    low = mid
            if ry[low] >= x:
                low += 1
            temp = min(low, temp)
            ans.append(temp)
        return ans

class Solution1:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # 后来发现这个数据存在特点，那就是y的量级是100
        ys = [[] for _ in range(101)]
        ymax = 1
        ans = []
        for x, y in rectangles:
            ys[y].append(x)
            ymax = max(ymax, y)
        for i in range(1, ymax + 1):
            ys[i].sort()
        for x, y in points:
            temp = 0
            for candidate in range(y, ymax + 1):
                if len(ys[candidate]) == 0:
                    continue
                low, high = 0, len(ys[candidate]) - 1
                while low < high:
                    mid = (low + high) // 2
                    if ys[candidate][mid] >= x:
                        high = mid
                    else:
                        low = mid + 1
                if ys[candidate][low] >= x:
                    low += 1
                temp += len(ys[candidate]) - low
                if ys[candidate][low] < x:
                    temp -= 1 # 当low在ys[candidate]最大索引上 可能是正好一个元素大于等于x，也有可能是所有元素都小于x
            ans.append(temp)
        return ans

def main():
    sol = Solution1()
    _input = ([[1, 2], [2, 3], [2, 5]], [[2, 1], [1, 4]])
    _input1 = ([[1, 1], [2, 2], [3, 3]], [[1, 3], [1, 1]])
    _output = sol.countRectangles(*_input1)
    print(_output)

if __name__ == '__main__':
    main()
