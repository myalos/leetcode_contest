# 题目
# 给你一个正整数num，请你统计并返回小于或等于num且各位数字之和为偶数的正整数的数目
# 正整数的各位数字之和是其所有位上的对应数字相加的结果
#
# 输入 num = 4
# 输入 2
# 2 和 4
# attemp 1 WA, input 4 output 0 expect 2
class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num + 1):
            x = i
            acc = 0
            while x > 0:
                acc += x % 10
                x /= 10
            if acc % 2 == 0:
                ans += 1
        return ans

# 错误原因 /=不是整除
class Solution1:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num + 1):
            x = i
            acc = 0
            while x > 0:
                acc += x % 10
                x //= 10
            if acc % 2 == 0:
                ans += 1
        return ans


def main():
    sol = Solution1()
    print(sol.countEven(4))

if __name__ == '__main__':
    main()
