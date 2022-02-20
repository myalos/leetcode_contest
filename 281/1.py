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
